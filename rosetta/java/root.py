from rosetta.java.type import JavaPackage
from rosetta.root import LanguageRoot


class JavaRoot(LanguageRoot):
    def __init__(self) -> None:
        self.packages: dict[str, JavaPackage] = {}
