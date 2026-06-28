import pytest


@pytest.fixture(params=["a", "b"])
def my_fixture(request):
    print(request.param)


def test_my_fixture(my_fixture):
    print("Login Successful")


@pytest.mark.parametrize("input1,input2,expected", [(1, 2, 3), (3, 4, 8), (5, 6, 10), (7, 8, 15)])
def test_addition(input1, input2, expected):
    assert input1 + input2 == expected
