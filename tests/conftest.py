from pytest import FixtureRequest, fixture

from src.data_capture.main import DataCapture
from src.interfaces.abc_datacapture import AbstractDataCapture
from src.interfaces.abc_statsbuilder import AbstractStatsBuilder


@fixture
def get_captured_data(request: FixtureRequest) -> AbstractDataCapture:
    capture = DataCapture()
    if getattr(request, "param", None):
        for val in request.param:
            capture.add(val)
    else:
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
    return capture


@fixture
def get_stats_operator(
    get_captured_data: AbstractDataCapture,
) -> AbstractStatsBuilder:
    return get_captured_data.build_stats()
