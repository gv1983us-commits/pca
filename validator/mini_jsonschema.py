"""
mini_jsonschema.py
-------------------
Vendored from MPAA commit 1d369f6cd091b99f9492cfaf730f0a170b55106e.
A small, dependency-free JSON Schema validator covering the subset
of Draft 2020-12 keywords used by the PCA Transition Record Schema:

    type, enum, const, pattern, format(date-time),
    minLength, maxLength, minItems, maxItems, uniqueItems, items,
    minProperties, propertyNames,
    properties, additionalProperties, required,
    allOf, anyOf, not, if/then/else, $ref, $defs

It deliberately does NOT try to be a general-purpose JSON Schema engine.
It exists so the validator has no external runtime dependency (no network,
no pip) and so every code path is auditable.

Design goal: never raise on malformed input. Always return a list of
JSONSchemaError instead.
"""

from __future__ import annotations

import datetime as _dt
import re
from dataclasses import dataclass, field
from typing import Any


_TYPE_MAP = {
    "object": dict,
    "array": list,
    "string": str,
    "boolean": bool,
    "null": type(None),
}

# RFC 3339 date-time, requiring a timezone designator (matches the schema's
# additional `"pattern": "Z$"` intent while being slightly more permissive
# about +HH:MM offsets, since the schema's own pattern only forces trailing Z).
_DATETIME_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})$"
)

_SUPPORTED_SCHEMA_KEYWORDS = {
    "$schema", "$id", "$ref", "$defs", "title", "description",
    "type", "enum", "const", "pattern", "format",
    "minLength", "maxLength", "minItems", "maxItems", "uniqueItems",
    "items", "minProperties", "propertyNames", "properties",
    "additionalProperties", "required", "allOf", "anyOf", "not",
    "if", "then", "else",
}


@dataclass
class JSONSchemaError:
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


@dataclass
class ValidationOutcome:
    errors: list = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return len(self.errors) == 0


def _type_matches(instance: Any, type_name: str) -> bool:
    if type_name == "integer":
        return isinstance(instance, int) and not isinstance(instance, bool)
    if type_name == "number":
        return isinstance(instance, (int, float)) and not isinstance(instance, bool)
    if type_name == "boolean":
        return isinstance(instance, bool)
    py_type = _TYPE_MAP.get(type_name)
    if py_type is None:
        return False  # fail closed on an unsupported schema type
    if type_name == "object":
        return isinstance(instance, dict)
    if type_name == "array":
        return isinstance(instance, list) and not isinstance(instance, str)
    return isinstance(instance, py_type) and not (
        type_name == "string" and isinstance(instance, bool)
    )


def _deep_equal(a: Any, b: Any) -> bool:
    return a == b and type(a) is type(b) if isinstance(a, bool) or isinstance(b, bool) else a == b


def _resolve(schema: dict, root: dict) -> dict:
    """Resolve a local JSON Pointer $ref, returning a fail-closed marker on error."""
    if not isinstance(schema, dict):
        return schema
    if "$ref" in schema:
        ref = schema["$ref"]
        if not isinstance(ref, str) or not ref.startswith("#/"):
            return {"__mini_schema_error__": f"unsupported external or malformed $ref: {ref!r}"}
        node: Any = root
        for raw_part in ref[2:].split("/"):
            part = raw_part.replace("~1", "/").replace("~0", "~")
            if not isinstance(node, dict) or part not in node:
                return {"__mini_schema_error__": f"unresolvable local $ref: {ref!r}"}
            node = node[part]
        if not isinstance(node, dict):
            return {"__mini_schema_error__": f"$ref target is not a schema object: {ref!r}"}
        siblings = {k: v for k, v in schema.items() if k != "$ref"}
        return {"allOf": [node, siblings]} if siblings else node
    return schema


class MiniValidator:
    """Validates instances against the given root JSON Schema document."""

    def __init__(self, schema: dict):
        self.root = schema

    def validate(self, instance: Any) -> list[JSONSchemaError]:
        errors: list[JSONSchemaError] = []
        self._audit_schema(self.root, "$schema", errors)
        if errors:
            return errors
        self._validate(instance, self.root, "$", errors)
        return errors

    def _audit_schema(self, schema: Any, path: str,
                      errors: list[JSONSchemaError]) -> None:
        """Reject unsupported/malformed schema constructs before validation."""
        if isinstance(schema, bool):
            return
        if not isinstance(schema, dict):
            errors.append(JSONSchemaError(path, "schema node must be an object or boolean"))
            return
        for key in schema:
            if key not in _SUPPORTED_SCHEMA_KEYWORDS:
                errors.append(JSONSchemaError(
                    path, f"unsupported schema keyword {key!r}; refusing to validate fail-open"
                ))

        allowed_types = set(_TYPE_MAP) | {"integer", "number"}
        if "type" in schema:
            declared = schema["type"]
            type_names = declared if isinstance(declared, list) else [declared]
            if (not type_names or any(
                    not isinstance(name, str) or name not in allowed_types
                    for name in type_names)):
                errors.append(JSONSchemaError(
                    f"{path}.type", f"unsupported or malformed type declaration {declared!r}"
                ))
        if "required" in schema and (
                not isinstance(schema["required"], list)
                or any(not isinstance(name, str) for name in schema["required"])):
            errors.append(JSONSchemaError(f"{path}.required", "must be an array of strings"))
        if "enum" in schema and not isinstance(schema["enum"], list):
            errors.append(JSONSchemaError(f"{path}.enum", "must be an array"))
        if "pattern" in schema:
            if not isinstance(schema["pattern"], str):
                errors.append(JSONSchemaError(f"{path}.pattern", "must be a string"))
            else:
                try:
                    re.compile(schema["pattern"])
                except re.error as exc:
                    errors.append(JSONSchemaError(f"{path}.pattern", f"invalid regex: {exc}"))
        if "format" in schema and schema["format"] != "date-time":
            errors.append(JSONSchemaError(
                f"{path}.format", f"unsupported format {schema['format']!r}"
            ))
        for key in ("minLength", "maxLength", "minItems", "maxItems", "minProperties"):
            if key in schema and (
                    not isinstance(schema[key], int) or isinstance(schema[key], bool)
                    or schema[key] < 0):
                errors.append(JSONSchemaError(
                    f"{path}.{key}", "must be a non-negative integer"
                ))
        if "uniqueItems" in schema and not isinstance(schema["uniqueItems"], bool):
            errors.append(JSONSchemaError(f"{path}.uniqueItems", "must be boolean"))

        if "$ref" in schema:
            resolved = _resolve(schema, self.root)
            if isinstance(resolved, dict) and "__mini_schema_error__" in resolved:
                errors.append(JSONSchemaError(path, resolved["__mini_schema_error__"]))
        for container in ("properties", "$defs"):
            value = schema.get(container)
            if value is not None:
                if not isinstance(value, dict):
                    errors.append(JSONSchemaError(f"{path}.{container}", "must be an object"))
                else:
                    for name, subschema in value.items():
                        self._audit_schema(subschema, f"{path}.{container}.{name}", errors)
        for key in ("items", "propertyNames", "additionalProperties", "not", "if", "then", "else"):
            if key in schema:
                self._audit_schema(schema[key], f"{path}.{key}", errors)
        for key in ("allOf", "anyOf"):
            if key not in schema:
                continue
            value = schema[key]
            if not isinstance(value, list):
                errors.append(JSONSchemaError(f"{path}.{key}", "must be an array"))
                continue
            for idx, subschema in enumerate(value):
                self._audit_schema(subschema, f"{path}.{key}[{idx}]", errors)

    # ------------------------------------------------------------------

    def _validate(self, instance: Any, schema: Any, path: str,
                  errors: list[JSONSchemaError]) -> None:
        if schema is True or schema == {}:
            return
        if schema is False:
            errors.append(JSONSchemaError(path, "schema forbids any value here"))
            return
        if not isinstance(schema, dict):
            return

        schema = _resolve(schema, self.root)
        if not schema:
            return
        if "__mini_schema_error__" in schema:
            errors.append(JSONSchemaError(path, schema["__mini_schema_error__"]))
            return

        # type
        if "type" in schema:
            types = schema["type"]
            types = types if isinstance(types, list) else [types]
            if not any(_type_matches(instance, t) for t in types):
                errors.append(JSONSchemaError(
                    path, f"expected type {types}, got {type(instance).__name__}"
                ))
                # Type mismatch usually makes the rest of the checks noise,
                # but we keep going for const/enum since those are cheap and
                # sometimes more informative than the type error alone.

        # const
        if "const" in schema:
            if not _deep_equal(instance, schema["const"]):
                errors.append(JSONSchemaError(
                    path, f"expected constant value {schema['const']!r}, got {instance!r}"
                ))

        # enum
        if "enum" in schema:
            if not any(_deep_equal(instance, v) for v in schema["enum"]):
                errors.append(JSONSchemaError(
                    path, f"value {instance!r} is not one of {schema['enum']!r}"
                ))

        # string constraints
        if isinstance(instance, str):
            if "minLength" in schema and len(instance) < schema["minLength"]:
                errors.append(JSONSchemaError(path, f"string shorter than minLength={schema['minLength']}"))
            if "maxLength" in schema and len(instance) > schema["maxLength"]:
                errors.append(JSONSchemaError(path, f"string longer than maxLength={schema['maxLength']}"))
            if "pattern" in schema:
                try:
                    if re.search(schema["pattern"], instance) is None:
                        errors.append(JSONSchemaError(
                            path, f"string {instance!r} does not match pattern {schema['pattern']!r}"
                        ))
                except re.error as exc:
                    errors.append(JSONSchemaError(path, f"invalid pattern in schema: {exc}"))
            if schema.get("format") == "date-time":
                valid_datetime = _DATETIME_RE.fullmatch(instance) is not None
                if valid_datetime:
                    try:
                        normalized = instance[:-1] + "+00:00" if instance.endswith("Z") else instance
                        _dt.datetime.fromisoformat(normalized)
                    except ValueError:
                        valid_datetime = False
                if not valid_datetime:
                    errors.append(JSONSchemaError(
                        path, f"string {instance!r} is not a valid RFC3339 date-time with timezone"
                    ))

        # array constraints
        if isinstance(instance, list):
            if "minItems" in schema and len(instance) < schema["minItems"]:
                errors.append(JSONSchemaError(path, f"array shorter than minItems={schema['minItems']}"))
            if "maxItems" in schema and len(instance) > schema["maxItems"]:
                errors.append(JSONSchemaError(path, f"array longer than maxItems={schema['maxItems']}"))
            if schema.get("uniqueItems"):
                seen = []
                for idx, item in enumerate(instance):
                    for other in seen:
                        if _deep_equal(item, other):
                            errors.append(JSONSchemaError(f"{path}[{idx}]", "duplicate item; uniqueItems=true"))
                            break
                    seen.append(item)
            if "items" in schema:
                for idx, item in enumerate(instance):
                    self._validate(item, schema["items"], f"{path}[{idx}]", errors)

        # object constraints
        if isinstance(instance, dict):
            if "minProperties" in schema and len(instance) < schema["minProperties"]:
                errors.append(JSONSchemaError(path, f"object has fewer than minProperties={schema['minProperties']}"))
            if "required" in schema:
                for key in schema["required"]:
                    if key not in instance:
                        errors.append(JSONSchemaError(path, f"missing required property '{key}'"))
            props = schema.get("properties", {})
            for key, subschema in props.items():
                if key in instance:
                    self._validate(instance[key], subschema, f"{path}.{key}", errors)
            if "propertyNames" in schema:
                for key in instance.keys():
                    self._validate(key, schema["propertyNames"], f"{path} (key '{key}')", errors)
            if "additionalProperties" in schema:
                ap = schema["additionalProperties"]
                extra = [k for k in instance.keys() if k not in props]
                if ap is False:
                    for key in extra:
                        errors.append(JSONSchemaError(path, f"unexpected property '{key}' (additionalProperties: false)"))
                elif isinstance(ap, dict):
                    for key in extra:
                        self._validate(instance[key], ap, f"{path}.{key}", errors)

        # allOf
        for sub in schema.get("allOf", []):
            self._validate(instance, sub, path, errors)

        # anyOf
        if "anyOf" in schema:
            branch_results = []
            for sub in schema["anyOf"]:
                sub_errors: list[JSONSchemaError] = []
                self._validate(instance, sub, path, sub_errors)
                branch_results.append(sub_errors)
            if not any(len(b) == 0 for b in branch_results):
                summary = "; ".join(
                    "/".join(str(e) for e in b) if b else "(ok)" for b in branch_results
                )
                errors.append(JSONSchemaError(path, f"none of the anyOf branches matched: {summary}"))

        # not
        if "not" in schema:
            sub_errors: list[JSONSchemaError] = []
            self._validate(instance, schema["not"], path, sub_errors)
            if not sub_errors:
                errors.append(JSONSchemaError(path, "instance matches a schema forbidden by 'not'"))

        # if / then / else
        if "if" in schema:
            cond_errors: list[JSONSchemaError] = []
            self._validate(instance, schema["if"], path, cond_errors)
            if not cond_errors:
                if "then" in schema:
                    self._validate(instance, schema["then"], path, errors)
            else:
                if "else" in schema:
                    self._validate(instance, schema["else"], path, errors)
