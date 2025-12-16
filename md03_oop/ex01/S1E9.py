from abc import ABC, abstractmethod


# Full Abstract Base Class (like interface)
class Character(ABC):
    """
    Base class for all characters.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Character instance.

        :param first_name: The first name of the character
        :type first_name: str
        :param is_alive: The state of being alive
        :type is_alive: bool
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Set the character's state to not alive.
        """
        self.is_alive = False


# Partial Abstract Class
# (which means it has concrete methods, and abstract method by inheritance)
class Stark(Character):
    """
    Class representing a Stark character.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Stark instance.

        :param first_name: The first name of the Stark character
        :type first_name: str
        :param is_alive: The state of being alive
        :type is_alive: bool
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Set the Stark character's state to not alive and print a message.
        """
        super().die()
