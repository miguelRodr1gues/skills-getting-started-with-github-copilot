import copy
import pytest
from fastapi.testclient import TestClient

import src.app as app_module
from src.app import app


@pytest.fixture(scope="session")
def client():
    """Session-scoped TestClient — one server instance for all tests."""
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def reset_activities():
    """
    Function-scoped, auto-use fixture.
    Deep-copies the in-memory activities dict before each test and
    restores it afterwards, keeping every test fully isolated.
    """
    original = copy.deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(original)
