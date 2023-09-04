"""
File_Name: fixtures_function_scope.py
Desc:
__copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 11/15/19
__modified__ = "Sharmila Vairamani" Changed the logging implementation - 04/27/2020
__modified__ = "Sharmila Vairamani" implemented thread storage to capture screenshots - 10/30/2020
__modified__ = "Sharmila Vairamani" removed autouse in the function browser - 11/04/2020

"""
import os
import threading

import pytest

from utilities.logger import Logger
from utilities.types import PageCreatorOld
from core.ui.browsers.browser_driver_factory import BrowserDriverFactory
from core.ui.browsers.head_less_browser import HeadLessBrowser
from core.ui.pages.page_factory import PageFactory
from core.ui.pages.page_type import PageType

logger = Logger(os.path.basename(__file__))


@pytest.fixture(scope='session')
def browser():
    """
    Function scope fixture  to return the currently configured web driver, which will
    be used by Allure for report generation
    :return: Selenium WebDriver
    """
    web_driver = HeadLessBrowser().create_web_driver()
    logger.debug("From browser, before calling web driver")
    # web_driver = BrowserDriverFactory.create_web_driver()

    logger.info("From browser, before yielding web driver")
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def function_browser(current_browser_type):
    """
    Function scope fixture to  return the currently configured web driver, which will
    be used by all function scope related test script fixtures.  These test scripts must
    be designed to handle each scenario in a separate browser instance.  If test scripts
    shares the  browser instance with other scenarios, session_browser must be used.
    :return: WebDriver
    """
    web_driver = BrowserDriverFactory.create_web_driver(current_browser_type)
    logger.debug("From function_browser, before yielding web driver in function_browser fixture")
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def page_builder(function_browser, ui_base_url, current_browser_type) -> PageCreatorOld:
    """
    Function scope fixture to return function handler, that builds/constructs
    the page for a given page type.
    :param ui_base_url:
    :param function_browser:
    :return: function
    """

    def get_page(page_type):
        logger.debug(f" From page_builder get_page for page_type : {page_type}")
        page = PageFactory.build_page(page_type, function_browser)
        thread_local = threading.current_thread()

        logger.debug(f" identity from get_page in page_builder=> {threading.get_ident()}")
        setattr(thread_local, 'test_page', page)
        logger.debug(f"{threading.get_ident()}")
        page = getattr(thread_local, 'test_page', None)

        if page is None:
            logger.debug("************************** page attribute is none in get_page  *************************")
        return page

    PageFactory.init_resources(base_url=ui_base_url, browser_type=current_browser_type)
    return get_page



@pytest.fixture(scope='function')
def sign_in_page(page_builder):
    """
    Function scope fixture to construct the Sign In screen page using the given function parameter (page_builder).
    :param page_builder: a fixture that gives a function to construct the page
    :return: SignInScreenPage
    """
    logger.debug("From function_sign_in_page fixture")
    sign_in_page = page_builder(PageType.SignInScreen)
    return sign_in_page






