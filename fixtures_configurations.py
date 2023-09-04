import os
from os.path import dirname
from typing import Dict

import pytest

from utilities.configuration_manager import ConfigurationManager, EnvironmentType

from utilities.logger import Logger
from core.ui.browsers.browser_type import BrowserType

logger = Logger(os.path.basename(__file__))


ConfigurationManager.init("DEFAULT")

@pytest.fixture(scope='session')
def environment_type():
    env = ConfigurationManager.get_environment()
    return EnvironmentType.from_string(env)


@pytest.fixture(scope='session')
def ui_base_url():
    return ConfigurationManager.get_base_url()


@pytest.fixture(scope='session')
def current_browser_type() -> BrowserType:
    return BrowserType.from_string(ConfigurationManager.get_active_browser())


@pytest.fixture(scope='session')
def results_folder():
    return os.path.join(dirname(os.path.realpath(__file__)), "results")
