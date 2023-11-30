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
        self.histogram = {}
        self.max_value = 0

    def add(self, value: int) -> None:
        self.histogram[value] = self.histogram[value] + 1 if value in self.histogram else 1  # O(1)
        self.max_value = value if value > self.max_value else self.max_value  # O(1)

    def build_stats(self) -> AbstractStatsBuilder:
        return self.stats_builder.load_data(histogram=self.histogram, max_value=self.max_value)  # O(n)
