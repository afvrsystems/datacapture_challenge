from collections import deque

from capture.interfaces.abc_datacapture import AbstractDataCapture
from capture.interfaces.abc_statsbuilder import AbstractStatsBuilder
from capture.stats_builder.main import StatsBuilder


class DataCapture(AbstractDataCapture):
    """Captures integer values and builds statistical operators.

    Args:
        stats_builder (AbstractStatsBuilder, optional): an instance of the statistical operator.
            It instantiates automatically a StatsBuilder by default.
    """

    def __init__(self, stats_builder: AbstractStatsBuilder = None) -> None:
        self.stats_builder = stats_builder or StatsBuilder()
        self.values = deque()

    def add(self, value: int) -> None:
        self.values.append(value)  # deque.append() has O(1) complexity

    def build_stats(self) -> AbstractStatsBuilder:
        return self.stats_builder.load_data(values=self.values)
