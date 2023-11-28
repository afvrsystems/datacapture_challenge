import numpy as np
from src.data_capture.main import DataCapture
from src.stats_builder.main import StatsBuilder
from tests.timing_tools import time_it
from pytest import mark
from .complexity_test_data import complexity_test_data


# @mark.parametrize("values,op_values,expected_slope,expected_r2", complexity_test_data)
# def test_data_capture_build_stats_complexity(values, op_values, expected_slope, expected_r2):
#     time_measurements = []
#     capture = DataCapture(stats_builder=StatsBuilder())

#     @time_it
#     def to_be_timed():
#         nonlocal capture
#         return capture.build_stats()
    
#     for val in values:
#         capture.add(val)
#         time_measurements.append(to_be_timed())

#     x, y = range(1, len(time_measurements) + 1), time_measurements
#     corr = np.corrcoef(x, y)
#     corr_xy = corr[0,1]
#     r_2 = corr_xy ** 2
#     slope = np.polyfit(x, y, 1)[0]
#     for x, y in zip(x, y):
#         print(x, y)
#     print(r_2)
#     print(slope)
    
#     assert False


@mark.parametrize("values,op_values,expected_slope,expected_r2", complexity_test_data)
def test_data_capture_less_complexity(values, op_values, expected_slope, expected_r2):
    time_measurements = []
    capture = DataCapture(stats_builder=StatsBuilder())

    @time_it
    def to_be_timed(stats: StatsBuilder):
        return stats.less(op_values[0])
    
    for val in values:
        capture.add(val)
        stats = capture.build_stats()
        time_measurements.append(to_be_timed(stats))

    x, y = range(1, len(time_measurements) + 1), time_measurements
    corr = np.corrcoef(x, y)
    corr_xy = corr[0,1]
    r_2 = corr_xy ** 2
    slope = np.polyfit(x, y, 1)[0]
    for x, y in zip(x, y):
        print(x, y)
    print(r_2)
    print(slope)
    
    assert False