from rosetta.java.root import JavaRoot
from rosetta.java.type import JavaPackage, JavaType, JavaField, JavaTypeReference, JavaExecutable, JavaReturn


def merge_lists_ignore_none[T, T2](a: list[T] | None, b: list[T2] | None) -> list[T | T2]:
    if a is None:
        return b if b is not None else []
    elif b is None:
        return a if a is not None else []
    else:
        return a + b


def merge_dicts_ignore_none[T, T2](a: dict[T] | None, b: dict[T2] | None) -> dict[T | T2]:
    if a is None:
        return b if b is not None else {}
    elif b is None:
        return a if a is not None else {}
    else:
        result: dict[T | T2] = {}
        result.update(a)
        result.update(b)
        return result


# TODO: not robust, breaks easily if the data is messed up

def parse_type_reference(raw: dict[str, any]) -> JavaTypeReference:
    # TODO: parse generics
    return JavaTypeReference(raw["basic"])


def parse_field(raw: dict[str, any]) -> JavaField:
    field = JavaField(raw["name"], parse_type_reference(raw["type"]))

    field.modifiers = set(raw.get("modifiers"))
    field.notes = raw.get("notes", "")
    field.deprecated = raw.get("deprecated", False)

    return field


def parse_return(raw: dict[str, any]) -> JavaReturn:
    return_ = JavaReturn(raw.get("name", "ret"), parse_type_reference(raw["type"]))

    return_.notes = raw.get("notes", "")

    return return_


def parse_executable(name: str, raw: dict[str, any]) -> JavaExecutable:
    executable = JavaExecutable(name)

    executable.modifiers = set(raw.get("modifiers", []))
    executable.returns = parse_return(raw["return"]) if raw.get("return") is not None else JavaReturn.VOID
    executable.notes = raw.get("notes", "")
    executable.deprecated = raw.get("deprecated", False)

    return executable


def parse_type(name: str, raw: dict[str, any]) -> JavaType:
    type = JavaType(name)
    type.java_type = raw["javaType"]
    if type.java_type == "class":
        type.extends = raw.get("extends", "Object")
    type.modifiers = set(raw.get("modifiers", []))
    type.notes = raw.get("notes", "")
    type.deprecated = raw.get("deprecated", False)

    fields = merge_dicts_ignore_none(raw.get("fields"), raw.get("staticFields"))
    for field in fields.values():
        field = parse_field(field)
        type.fields[field.name] = field

    methods = merge_lists_ignore_none(raw.get("methods"), raw.get("staticMethods"))
    for method in methods:
        method = parse_executable(method["name"], method)
        type.methods[method.name] = method

    constructors = raw.get("constructors")
    if constructors is not None:
        for constructor in constructors:
            type.constructors.append(
                parse_executable("<ctor>", constructor)
            )

    return type


def parse_package(name: str, raw: dict[str, any]) -> JavaPackage:
    package = JavaPackage(name)

    for name, data in raw.items():
        package.types.append(
            parse_type(name, data)
        )

    return package


def parse_root(root: JavaRoot, raw: dict[str, any]) -> JavaRoot:
    if (packages := raw.get("packages")) is not None:
        for name, package in packages.items():
            root.packages[name] = parse_package(name, package)

    return root
