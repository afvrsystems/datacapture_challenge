from pytest import fixture

from src.data_capture.main import DataCapture
from src.interfaces.abc_datacapture import AbstractDataCapture
from src.interfaces.abc_statsbuilder import AbstractStatsBuilder
from src.stats_builder.main import StatsBuilder


@fixture
def get_stats_builder() -> AbstractDataCapture:
    return StatsBuilder()


@fixture
def get_some_captured_data(get_stats_builder) -> AbstractDataCapture:
    capture = DataCapture(get_stats_builder)
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    return capture


@fixture
def get_stats_operator(
    get_some_captured_data: AbstractDataCapture,
) -> AbstractStatsBuilder:
    return get_some_captured_data.build_stats()
