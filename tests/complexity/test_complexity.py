from random import randint

import numpy as np
import pytest

from src.data_capture.main import DataCapture
from src.stats_builder.main import StatsBuilder
from tests.timing_tools import get_timing


def get_r2_and_slope(values: list[float]) -> tuple[float]:
    x, y = range(1, len(values) + 1), values
    corr = np.corrcoef(x, y)
    corr_xy = corr[0, 1]
    return np.polyfit(x, y, 1)[0], corr_xy**2


@pytest.mark.skip(reason="This test should be launched manually from console.")
def test_data_capture_build_stats_complexity():
    values = [randint(1, 1000) for _ in range(500)]
    time_measurements = []
    capture = DataCapture(stats_builder=StatsBuilder())

    for i, val in enumerate(values):
        capture.add(val)
        with get_timing() as timing:
            _ = capture.build_stats()
        timed = timing()
        time_measurements.append(timed)
        print(i, val, timed, len(capture.values))

    slope, r_2 = get_r2_and_slope(time_measurements)
    print(r_2)
    print(slope)


@pytest.mark.skip(reason="This test should be launched manually from console.")
def test_data_capture_comparisons_complexity():
    values = [randint(1, 1000) for _ in range(500)]
    start_value = randint(1, 500)
    end_value = randint(500, 1000)

    time_measurements = []
    capture = DataCapture(stats_builder=StatsBuilder())

    for i, val in enumerate(values):
        capture.add(val)
        stats = capture.build_stats()
        with get_timing() as timing:
            _ = stats.less(start_value)
            # _ = stats.greater(start_value)
            # _ = stats.between(start_value, end_value)
        timed = timing()
        time_measurements.append(timed)
        print(i, val, timed)

    slope, r_2 = get_r2_and_slope(time_measurements)
    print(r_2)
    print(slope)


if __name__ == "__main__":
    test_data_capture_build_stats_complexity()
    test_data_capture_comparisons_complexity()
