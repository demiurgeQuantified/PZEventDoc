from __future__ import annotations

from typing import Type, TYPE_CHECKING
if TYPE_CHECKING:
    from eventdoc.rendering.renderers.base_renderer import BaseRenderer


renderers: dict[str, Type[BaseRenderer]] = {}


def get_renderer_class(name: str) -> Type[BaseRenderer] | None:
    return renderers.get(name)


def get_renderer(name: str) -> BaseRenderer | None:
    renderer_class = get_renderer_class(name)
    if renderer_class is None:
        return None

    return renderer_class(name)


def register_renderer(generator_class: Type[BaseRenderer], names: list[str]):
    """
    Registers a class as the generator for a file extension

    :param generator_class: The class to handle these extensions with
    :param names: List of names to register this generator under
    :return:
    """
    for name in names:
        renderers[name] = generator_class
