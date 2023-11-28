from abc import ABC, abstractmethod

from src.interfaces.abc_statsbuilder import AbstractStatsBuilder


class AbstractDataCapture(ABC):
    @abstractmethod
    def __init__(self, stats_builder: AbstractStatsBuilder = None) -> None:
        """Captures integer values and builds statistical operators.

        Args:
            stats_builder (AbstractStatsBuilder): an instance of the statistical operator.
        """

    @abstractmethod
    def add(self, value: int) -> None:
        """Adds an integer value to the data list.

        Args:
            value (int): the integer value to be added.
        """

    @abstractmethod
    def build_stats(self) -> AbstractStatsBuilder:
        """Populates an instance of a statistical operator.

        Returns:
            AbstractStatsBuilder: an instance that applies statistical operations on captured data.
        """
