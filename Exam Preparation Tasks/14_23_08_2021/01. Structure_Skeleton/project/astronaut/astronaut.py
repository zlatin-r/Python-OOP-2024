from abc import ABC, abstractmethod
from typing import List


class Astronaut(ABC):

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack: List = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self):
        pass

    def increase_oxygen(self, amount: int) -> None:
        self.oxygen += amount
