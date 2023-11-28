from abc import ABC, abstractmethod


class AbstractStatsBuilder(ABC):
    @abstractmethod
    def __init__(self) -> None:
        """Applies statistical operations on data."""

    @abstractmethod
    def load_data_freqs(self, data_freqs: dict[int, int]) -> None:
        """Loads the data frequencies (histogram).

        Args:
            data_freqs (dict[int, int]): the data's histogram.
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
