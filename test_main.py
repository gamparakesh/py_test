from basic.main import get_weather


def test_get_weather():
    assert get_weather(21) == "cold"
