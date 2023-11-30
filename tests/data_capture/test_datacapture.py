from random import randint

import pytest

from capture.data_capture.main import DataCapture
from capture.interfaces.abc_statsbuilder import AbstractStatsBuilder
from tests.test_data import data_for_testing


def test_data_capture_build_stats(get_captured_data):
    stats = get_captured_data.build_stats()
    assert isinstance(stats, AbstractStatsBuilder)


@pytest.mark.parametrize(
    "get_captured_data,max_value,less_dict,hist,inputs,expected",
    data_for_testing,
    indirect=["get_captured_data"],
)
def test_data_capture_instance_variables(
    get_captured_data,
    max_value,
    less_dict,
    hist,
    inputs,
    expected,
):
    assert get_captured_data.histogram == hist
    assert get_captured_data.max_value == max_value


@pytest.mark.parametrize(
    "captured_data",
    [[randint(1, 100) for _ in range(i * 100)] for i in range(1, 11)],
)
def test_capture_random_values(captured_data):
    max_value = max(captured_data)
    hist = {num: captured_data.count(num) for num in set(captured_data)}
    hist_acc = {}
    for num in range(1, max_value + 1):
        hist_acc[num] = hist.get(num, 0) + hist_acc.get(num - 1, 0)
    less_dict = {num: hist_acc.get(num - 1, 0) for num in hist_acc.keys()}
    less = randint(1, 50)

    capture = DataCapture()
    for num in captured_data:
        capture.add(num)
    stats = capture.build_stats()
    assert stats.less_than_index == less_dict
    assert stats.histogram == hist
    assert stats.max_value == max_value
    assert stats.less(less) == less_dict[less] if less <= max_value else len(captured_data)
