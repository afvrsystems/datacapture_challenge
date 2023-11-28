import pytest

from tests.stats_builder.test_data import data_for_testing


@pytest.mark.parametrize(
    "get_captured_data,less_dict,greater_dict,hist,inputs,expected",
    data_for_testing,
    indirect=["get_captured_data"],
)
def test_statsbuilder_less(
    get_stats_operator,
    get_captured_data,
    less_dict,
    greater_dict,
    hist,
    inputs,
    expected,
):
    assert get_stats_operator.less(inputs[0]) == expected[0]


@pytest.mark.parametrize(
    "get_captured_data,less_dict,greater_dict,hist,inputs,expected",
    data_for_testing,
    indirect=["get_captured_data"],
)
def test_statsbuilder_greater(
    get_stats_operator,
    get_captured_data,
    less_dict,
    greater_dict,
    hist,
    inputs,
    expected,
):
    assert get_stats_operator.greater(inputs[1]) == expected[1]


@pytest.mark.parametrize(
    "get_captured_data,less_dict,greater_dict,hist,inputs,expected",
    data_for_testing,
    indirect=["get_captured_data"],
)
def test_statsbuilder_between(
    get_stats_operator,
    get_captured_data,
    less_dict,
    greater_dict,
    hist,
    inputs,
    expected,
):
    assert get_stats_operator.between(inputs[2], inputs[3]) == expected[2]


@pytest.mark.parametrize(
    "get_captured_data,less_dict,greater_dict,hist,inputs,expected",
    data_for_testing,
    indirect=["get_captured_data"],
)
def test_statsbuilder_load_data(
    get_stats_operator,
    get_captured_data,
    less_dict,
    greater_dict,
    hist,
    inputs,
    expected,
):
    assert get_stats_operator.less_than_index == less_dict
    assert get_stats_operator.greater_than_index == greater_dict
    assert get_stats_operator.histogram == hist


def test_monad_pattern(get_captured_data):
    assert get_captured_data.build_stats().less(4) == 2
