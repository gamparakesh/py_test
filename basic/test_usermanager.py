import pytest
from usermanager import usermanager


@pytest.fixture(name="user_manager")
def _user_manager_fixture():
    return usermanager()


def test_add_user(user_manager):
    user_manager.add_user("jane_doe", "john@example.com")
    assert user_manager.get_user("jane_doe") == "john@example.com"


def test_add_duplicate_user(user_manager):
    user_manager.add_user("jane_doe", "jane@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("jane_doe", "jane@example.com")
