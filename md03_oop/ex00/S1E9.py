from abc import ABC, abstractmethod

class Character(ABC):
    abstractmethod
    @abstractmethod
    def attack(self):
        pass

class Start(Character):
