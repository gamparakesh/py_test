import pytest


@pytest.fixture(name="my_fixture", params=["a", "b"])
def _my_fixture(request):
    return request.param


def test_my_fixture(my_fixture):
    assert my_fixture in ["a", "b"]


@pytest.mark.parametrize("input1,input2,expected", [(1, 2, 3), (3, 4, 7), (5, 6, 11), (7, 8, 15)])
def test_addition(input1, input2, expected):
    assert input1 + input2 == expected
