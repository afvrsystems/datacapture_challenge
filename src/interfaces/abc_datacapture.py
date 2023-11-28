from abc import ABC, abstractmethod

from src.interfaces.abc_statsbuilder import AbstractStatsBuilder


class AbstractDataCapture(ABC):
    """This is a blueprint for data capture classes."""

    @abstractmethod
    def __init__(self, stats_builder: AbstractStatsBuilder = None) -> None:
        ...

    @abstractmethod
    def add(self, value: int) -> None:
        """Adds a new integer value to the data.

        Args:
            value (int): the integer value to be added.
        """

    @abstractmethod
    def build_stats(self) -> AbstractStatsBuilder:
        """Populates an instance of statistical operator.

        Returns:
            AbstractStatsBuilder: an instance that applies statistical operations on captured data.
        """
