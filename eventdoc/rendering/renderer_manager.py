from __future__ import annotations

from typing import Type, TYPE_CHECKING
if TYPE_CHECKING:
    from eventdoc.rendering.renderers.base_renderer import BaseRenderer


renderers: dict[str, Type["BaseRenderer"]] = {}


def get_renderer_class(extension: str) -> Type["BaseRenderer"] | None:
    return renderers.get(extension)


def get_renderer(extension: str) -> BaseRenderer | None:
    renderer_class = get_renderer_class(extension)
    if renderer_class is None:
        return None

    return renderer_class()


def register_renderer(generator_class: Type["BaseRenderer"], extensions: list[str]):
    """
    Registers a class as the generator for a file extension

    :param generator_class: The class to handle these extensions with
    :param extensions: List of file extensions to register this generator for
    :return:
    """
    for extension in extensions:
        renderers[extension] = generator_class
