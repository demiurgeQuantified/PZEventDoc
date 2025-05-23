from __future__ import annotations

from typing import ClassVar

from rosetta.object import RosettaObject


class JavaTypeReference:
    def __init__(self, basic: str, generics: list[JavaTypeReference] | None = None) -> None:
        self.basic: str = basic
        self.generics: list[JavaTypeReference] = generics if generics is not None else []


class JavaParameter(RosettaObject):
    def __init__(self, name: str, type: JavaTypeReference) -> None:
        super().__init__(name)
        self.type: JavaTypeReference = type


class JavaReturn(RosettaObject):
    VOID: ClassVar[JavaReturn]

    def __init__(self, name: str, type: JavaTypeReference) -> None:
        super().__init__(name)
        self.type: JavaTypeReference = type


class JavaExecutable(RosettaObject):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.modifiers: set[str] = set()
        self.parameters: list[JavaParameter] = []
        self.returns: JavaReturn = JavaReturn.VOID


class JavaField(RosettaObject):
    def __init__(self, name: str, type: JavaTypeReference) -> None:
        super().__init__(name)
        self.type: JavaTypeReference = type


class JavaType(RosettaObject):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.extends: str = ""
        # This is kept as a string because we can't guarantee the supertype is actually loaded.
        self.java_type: str = ""
        """e.g. 'class', 'interface'"""
        self.fields: dict[str, JavaField] = {}
        self.constructors: list[JavaExecutable] = []
        self.methods: dict[str, JavaExecutable] = {}
        self.modifiers: set[str] = set()


class JavaPackage(RosettaObject):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.types: list[JavaType] = []


JavaReturn.VOID = JavaReturn("", JavaTypeReference("void"))
