from src.interfaces.abc_datacapture import AbstractDataCapture
from src.interfaces.abc_statsbuilder import AbstractStatsBuilder


def test_statsbuilder_less(get_stats_operator: AbstractStatsBuilder):
    assert get_stats_operator.less(4) == 2


def test_statsbuilder_greater(get_stats_operator: AbstractStatsBuilder):
    assert get_stats_operator.greater(4) == 2


def test_statsbuilder_less(get_stats_operator: AbstractStatsBuilder):
    assert get_stats_operator.between(3, 6) == 4


def test_chain(get_some_captured_data: AbstractDataCapture):
    assert get_some_captured_data.build_stats().less(4) == 2
