from src.interfaces.abc_datacapture import AbstractDataCapture
from src.interfaces.abc_statsbuilder import AbstractStatsBuilder


def test_data_capture_values(get_some_captured_data: AbstractDataCapture):
    assert get_some_captured_data.values == [3, 9, 3, 4, 6]


def test_data_capture_histogram(get_some_captured_data: AbstractDataCapture):
    values = get_some_captured_data.values
    assert get_some_captured_data.get_histogram(values) == {3: 2, 9: 1, 4: 1, 6: 1}


def test_data_capture_build_stats(get_some_captured_data: AbstractDataCapture):
    stats = get_some_captured_data.build_stats()
    assert isinstance(stats, AbstractStatsBuilder)
