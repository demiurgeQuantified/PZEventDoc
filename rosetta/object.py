class RosettaObject:
    def __init__(self, name: str):
        self.name: str = name
        self.notes: str = ""
        self.deprecated: bool = False
        self.tags: list[str] = []
