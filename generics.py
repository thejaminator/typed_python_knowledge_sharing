from abc import ABC, abstractmethod
from typing import TypeVar, List

# Generics
A = TypeVar("A")


def list_into_set(the_list: list[A]) -> set[A]:
    return set(the_list)


list_into_set([1, 2, 3])
list_into_set(["meow"])

# Upper bound generics


class Animal(ABC):  # Abstract base class Animal
    ...  # three dots means its just a stub. Equivalent to scala ???


class Dog(Animal):
    ...


class Cat(Animal):
    ...


B = TypeVar("B", bound=Animal)


def do_something_with_animal_no_generic(animal: Animal) -> Animal:
    return animal


def do_something_with_animal(animal: B) -> B:
    return animal


do_something_with_animal_no_generic(Dog())  # infers Animal
do_something_with_animal(Dog())  # infers Dog
do_something_with_animal(Cat())  # infers Cat
do_something_with_animal("i'm not an animal")

# Variance


def upload_animals(animals: List[Animal]) -> None:
    return None


animals: list[Dog] = [Dog()]
upload_animals(animals)  # Why doesn't this work?


B_co = TypeVar("B_co", covariant=True)


class DangerouslyCovariantList(list[B_co]):
    ...


def many_animals_co(animals: DangerouslyCovariantList[Animal]) -> None:
    return None


co_animals: DangerouslyCovariantList[Dog] = DangerouslyCovariantList([Dog()])
many_animals_co(co_animals) # yay!
