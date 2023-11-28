from collections import deque

from capture.interfaces.abc_statsbuilder import AbstractStatsBuilder


class StatsBuilder(AbstractStatsBuilder):
    """Generates statistics from previously loaded data."""

    def __init__(self) -> None:
        self.less_than_index = {}
        self.greater_than_index = {}
        self.histogram = {}
        self.max_value = 0
        self.total_value_qty = 0

    def load_data(self, values: deque) -> AbstractStatsBuilder:  # dict().get() has O(1) complexity
        self.clear()  # dict.clear() has O(1) complexity
        max_value = max(values)  # max() has O(n) complexity
        max_value_iter = range(1, max_value + 1)  # iterable building has O(1) complexity
        self.total_value_qty = len(values)  # len() has O(1) complexity
        self.histogram = {n: 0 for n in max_value_iter}  # dict comprehension has O(n) complexity

        for val in values:  # for-loop has O(n) complexity
            self.histogram[val] += 1

        for num in max_value_iter:  # for-loop has O(n) complexity
            self.less_than_index[num] = self.histogram[num] + self.less_than_index.get(
                num - 1, 0
            )  # dict.get() has O(1) complexity

        self.less_than_index = {  # for-loop has O(n) complexity
            num: self.histogram[num] + self.less_than_index.get(num - 1, 0)  # dict.get() has O(1) complexity
            for num in max_value_iter
        }

        for num in max_value_iter:  # for-loop has O(n) complexity
            self.less_than_index[num] -= self.histogram[num]  # dict.get() has O(1) complexity
            self.greater_than_index[num] = (  # dict.get() has O(1) complexity
                self.total_value_qty - self.histogram[num] - self.less_than_index[num]
            )

        return self

    def less(self, value: int) -> int:  # dict().get() has O(1) complexity
        return self.less_than_index[value] if value <= self.max_value else self.total_value_qty

    def greater(self, value: int) -> int:  # dict().get() has O(1) complexity
        return self.greater_than_index[value] if value <= self.max_value else 0

    def between(self, start_val: int, end_val: int) -> int:  # dict().get() has O(1) complexity
        return self.greater(start_val) - self.greater(end_val) + self.histogram.get(start_val, 0)

    def clear(self) -> None:
        self.less_than_index.clear()
        self.greater_than_index.clear()
        self.histogram.clear()
        self.max_value = 0
        self.total_value_qty = 0
