import pytest
from core.ui.drivers.playground_driver import PlaygroundDriver


@pytest.fixture(scope='session')
def playground_driver():
    return PlaygroundDriver()



