import importlib
import os
from logging import config

import pytest

from config.logger_config import get_log_config
from utilities.configuration_manager import ConfigurationManager
from utilities.logger import Logger

plugins = ['fixtures_configurations', 'fixtures_function_scope', 'fixtures_session_scope',
            'fixtures_ui_drivers', 'fixtures_ui_pages']
# system_related_plugins = ['fixtures_zmq_driver_asserts', 'fixtures_zmq_drivers', 'fixtures_win_app_driver', 'fixtures_empower_drivers']

logger = Logger(os.path.basename(__file__))


@pytest.fixture(scope='function')
def context():
    return {}


@pytest.fixture()
def assert_timeout():
    from utilities.assert_timeout import AssertTimeout
    return AssertTimeout()


def configure_logger():
    log_config = get_log_config(log_file_suffix="pytest")
    if not os.path.exists("./results"):
        os.mkdir("./results")
    log_config['handlers']['debug_file_handler']['filename'] = os.path.join('results',
                                                                            log_config['handlers']['debug_file_handler']['filename'])

    log_config['handlers']['error_file_handler']['filename'] = os.path.join('results',
                                                                            log_config['handlers']['error_file_handler']['filename'])

    config.dictConfig(log_config)


def pytest_addoption(parser):
    parser.addoption("--environment", action="store", default="SIMULATION", choices=["SIMULATION", "REAL", "CDS"],
                     help="Type of target environment, simulation is default")
    parser.addoption("--local_run", action="store_true", default=False, help="Run without system related plugins")


def pytest_configure(config):
    for plugin in plugins:
        config.pluginmanager.register(importlib.import_module(plugin))
    