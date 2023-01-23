from typing import Any


class Animal:
    def __init__(self, name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> Any:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> Any:
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str,
                 appetite: int = 3,
                 is_hungry: bool = True) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse() -> Any:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str,
                 appetite: int = 7,
                 is_hungry: bool = True) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> Any:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    appetit_animals = 0
    for animal in animals:
        if isinstance(animal, Animal):
            appetit_animals += animal.feed()
            Animal.feed(animal)
    return appetit_animals
