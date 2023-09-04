"""
File_Name: fixtures_session_scope.py
Desc:

__copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 11/15/19
__modified__ = "Sharmila Vairamani" Changed the logging implementation-04/27/2020
__modified__ = "Sharmila Vairamani" Removed the attribute for the implicit wait-05/28/2020
__modified__ = "Sharmila Vairamani" implemented thread storage to capture screenshots  - 10/30/2020
__modified__= "Sharmila Vairamani" Added session_command_screen_page function - 05/20/2021
"""
import os

import pytest

from utilities.configuration_manager import EnvironmentType
from utilities.logger import Logger
from core.ui.pages.page_factory import PageFactory

logger = Logger(os.path.basename(__file__))


@pytest.fixture(scope='session')
def session_browser(current_browser_type):
    """
    Session scope fixture to  return the currently configured web driver, which will
    be used by all session scope related test script fixtures.  These test scripts must
    be designed to handle multiple scenarios in a separate browser instance.  If test scripts
    needs individual instance of browser/WebDriver with each scenarios, function_browser must be used.
    :return:WebDriver
    """
    logger.debug("within conftest::session_browser")
    session_driver = PageFactory.create_session_driver(current_browser_type)
    logger.debug("within conftest::session_browser, after create_session_driver")
    return session_driver



