from src.data_capture.main import DataCapture
from src.interfaces.abc_statsbuilder import AbstractStatsBuilder


def test_data_capture_values():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    assert list(capture.values) == [3, 9, 3, 4, 6]


def test_data_capture_build_stats(get_captured_data):
    stats = get_captured_data.build_stats()
    assert isinstance(stats, AbstractStatsBuilder)
