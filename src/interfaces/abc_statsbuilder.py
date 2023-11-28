from abc import ABC, abstractmethod
from collections import deque


class AbstractStatsBuilder(ABC):
    """This is a blueprint for statistical operator classes."""

    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def load_data(self, values: deque) -> None:
        """Loads the data that is going to be operated.

        Args:
            values (deque): the queue of captured values.
        """

    @abstractmethod
    def less(self, value: int) -> int:
        """Counts how many values are less than the given value.

        Args:
            value (int): the given value.

        Returns:
            int: the quantity of values that are less than the given value.
        """

    @abstractmethod
    def between(self, start_val: int, end_val: int) -> int:
        """Counts how many values
        are greater than or equal to the starting value and how many
        are greater than or equal to the ending value.
        This is equivalent to an inclusive-range counter (intersection).

        Args:
            start_val (int): the starting value of the range.
            end_val (int): the ending value of the range.

        Returns:
            int: the quantity of values that are in the range.
        """

    @abstractmethod
    def greater(self, value: int) -> int:
        """Counts how many values are greater than the given value.

        Args:
            value (int): the given value.

        Returns:
            int: the quantity of values that are greater than the given value.
        """
