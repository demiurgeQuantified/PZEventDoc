from importlib.resources.abc import Traversable

import kirjava
from kirjava import InsnBlock, Frame, Entry
from kirjava.instructions import InvokeInstruction, ConstantInstruction
from kirjava.source import InstructionInBlock
from kirjava.types import null_t, string_t, object_t

from .result import EventInvocation, Event


def resolve_stack_string(entry: Entry) -> str:
    """
    Resolves the value of a string stack entry.
    :param entry: Stack entry containing a string.
    :return: The value of the stack entry.
    """
    if len(entry.producers) > 1:
        print("More than one producer, this event is scary")
    # currently fails if it's not a constant, probably don't care
    producer = entry.producers[0]
    assert isinstance(producer, InstructionInBlock)
    assert isinstance(producer.instruction, ConstantInstruction)
    assert producer.instruction.constant.type is string_t
    return producer.instruction.constant.value


def infer_type(entry: Entry) -> str:
    types = entry.inference()
    for type in types:
        if type is null_t:
            # null is always a possible type, ignore it
            continue
        if type is object_t:
            # this is the least specific type so ignore it unless it's the only one
            continue
        # if null_t in types:
        #     return type.name + "?"
        # else:
        return type.name
    if object_t in types:
        return object_t.name

    return "null"
    # FIXME: this still sometimes returns the wrong types
    #  in complex methods, likely compiler optimisations make this return unrelated types
    #  for perfect type inference, may need to actually follow the stack and determine what must be on it at that moment
    """
zombie/iso/IsoWorld#init triggers event OnNewGame with arguments ['java/lang/Object', 'zombie/iso/IsoGridSquare'].
zombie/iso/IsoWorld#init triggers event OnNewGame with arguments ['null', 'java/util/Iterator'].
    """


trigger_event_names: set[str] = {"triggerEvent", "triggerEventGarbage", "triggerEventUnique"}


def analyse_java(path: Traversable) -> list[Event]:
    with path.open('rb') as stream:
        clazz = kirjava.ClassFile.read(stream)

    invocations: list[EventInvocation] = []

    for method in clazz.methods:
        if method.is_abstract or method.is_native:
            continue
        if method.name in trigger_event_names:
            # print(f"Ignoring method named triggerEvent in class {clazz.name}")
            # these usually pass through an event name so they aren't useful
            continue
        graph = kirjava.disassemble(method)
        trace = kirjava.trace(graph)
        for block in graph.blocks:
            if not isinstance(block, InsnBlock):
                continue
            for instruction in block.instructions:
                if not isinstance(instruction, InvokeInstruction):
                    continue
                if instruction.reference.name in trigger_event_names \
                        and instruction.reference.class_.name == "zombie/Lua/LuaEventManager":
                    frame: Frame | None = None
                    for context in trace.retrace(block, trace.entries[block][0]):
                        if isinstance(context.source, InstructionInBlock) and context.source.instruction is instruction:
                            break
                        frame = context.frame.copy()

                    assert frame is not None
                    assert frame.stack[0].type is string_t

                    invocation = EventInvocation(
                        name=resolve_stack_string(frame.stack[0])
                    )
                    for argument in frame.stack[1:]:
                        invocation.arguments.append(infer_type(argument))
                    invocations.append(invocation)

                    # print(f"{clazz.name}#{method.name} triggers event {invocation.name} with arguments {invocation.arguments}.")

    events: dict[str, Event] = {}

    for invocation in invocations:
        event = events.get(invocation.name)
        if event is None:
            event = Event(invocation.name)
            events[invocation.name] = event
        event.arguments.append(invocation.arguments)

    return list(events.values())
