"""Duck typing | Protocol | Structural types"""
from typing import Protocol, TypeVar


def sort_untyped(stuff):
    """Returns a new sorted iterable"""
    new = stuff.copy()  # i hope it implements copy....
    sorted(
        new
    )  # will explode if the items inside don't implement __lt__ !!!! also sorted mutates in place lmao
    return new


Sortable = TypeVar("Sortable", bound="Comparable")

class Comparable(Protocol):
    def __lt__(self: Sortable, other: Sortable) -> bool:
        pass


def sort(stuff: list[Sortable]) -> list[Sortable]:
    """
    Returns a new sorted list"""
    new = stuff.copy()
    sorted(new)
    return new


sort([1, 2, 3])
sort([{"a_dict": 2}, {"a_dict": 2}]) # type error
