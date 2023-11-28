from collections import deque

from src.interfaces.abc_datacapture import AbstractDataCapture
from src.interfaces.abc_statsbuilder import AbstractStatsBuilder
from src.stats_builder.main import StatsBuilder


class DataCapture(AbstractDataCapture):
    def __init__(self, stats_builder: AbstractStatsBuilder = None) -> None:
        self.stats_builder = stats_builder or StatsBuilder()
        self.values = deque()

    def add(self, value: int) -> None:
        self.values.append(value)  # deque.append() has O(1) complexity

    def build_stats(self) -> AbstractStatsBuilder:
        return self.stats_builder.load_data(values=self.values)
