class LanguageRoot:
    ...


class RosettaRoot:
    def __init__(self) -> None:
        # FIXME: not sure how to strongly type this in an expandable way
        self.games: dict[str, any] = {}
        self.languages: dict[str, LanguageRoot] = {}
