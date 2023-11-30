from capture.interfaces.abc_statsbuilder import AbstractStatsBuilder


class StatsBuilder(AbstractStatsBuilder):
    """Generates statistics from previously loaded data."""

    def __init__(self) -> None:
        self.less_than_index = {}
        self.histogram = {}
        self.hist_accumulator = 0
        self.max_value = 0

    def load_data(self, histogram: dict, max_value: int) -> AbstractStatsBuilder:
        self.clear()  # O(1)
        self.max_value = max_value
        self.histogram = histogram

        for num in range(1, self.max_value + 1):  # O(n)
            self.less_than_index[num] = self.hist_accumulator  # O(1)
            self.hist_accumulator += self.histogram.get(num, 0)  # O(1)

        return self

    def less(self, value: int) -> int:  # O(1)
        return self.less_than_index[value] if value <= self.max_value else self.hist_accumulator

    def greater(self, value: int) -> int:  # O(1)
        return (
            self.hist_accumulator - self.histogram[value] - self.less_than_index[value]
            if value <= self.max_value
            else 0
        )

    def between(self, start_val: int, end_val: int) -> int:  # O(1)
        return self.less(end_val) - self.less(start_val) + self.histogram.get(end_val, 0)

    def clear(self) -> None:
        self.less_than_index.clear()  # O(1)
        self.histogram.clear()  # O(1)
        self.hist_accumulator = 0
        self.max_value = 0
