from __future__ import annotations
from typing import Optional


class Animal():
    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: Optional[bool] = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> str:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: Optional[bool] = True) -> None:
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: Optional[bool] = True) -> None:
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> str:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    return sum(beast.feed() for beast in animals)
