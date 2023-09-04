"""
File_Name: page_factory.py
Desc: This file contains creation of different pages and injecting the _driver into the created pages
"""

import copy
import threading

from utilities.logger import Logger
from core.ui.browsers.browser_driver_factory import BrowserDriverFactory
from core.ui.pages.playground_page import PlayGroundScreen
from core.ui.pages.page_type import PageType

logger = Logger("page_factory")


class PageFactory:
    page_dictionary = None

    @classmethod
    def init_pages(cls, driver, base_url):
        cls.page_dictionary = {
            PageType.PlayGroundScreen: PlayGroundScreen(driver=driver, base_url=base_url)
        }

    function_cope_page_types = [PageType.PlayGroundScreen
                            ]
    session_driver = None
    session_driver_lock = threading.Lock()

    @classmethod
    def configure_page(cls, page, driver):
        page.set_driver(driver)

    @classmethod
    def create_session_driver(cls, browser_type):
        if cls.session_driver is not None:
            return cls.session_driver

        try:
            cls.session_driver_lock.acquire()
            local_driver = BrowserDriverFactory.create_web_driver(browser_type=browser_type)
            logger.debug("From create_session_driver, after creating web_driver")

            cls.session_driver = local_driver
        finally:
            cls.session_driver_lock.release()

        return cls.session_driver

    @classmethod
    def init_resources(cls, base_url, browser_type):
        cls.init_pages(driver=None, base_url=base_url)
        if cls.session_driver is None:
            cls.session_driver = cls.create_session_driver(browser_type)
        for page_type in cls.page_dictionary:
            page = cls.page_dictionary[page_type]
            cls.configure_page(page, cls.session_driver)

    @classmethod
    def get_page(cls, page_type):
        if page_type in cls.page_dictionary:
            page = cls.page_dictionary[page_type]
            return page
        return None

    @classmethod
    def build_page(cls, page_type, web_driver):

        if page_type in cls.page_dictionary:
            # Only for Function scope pages (i.e. pages that require its own copy and doesn't share)
            if page_type in cls.function_cope_page_types:
                page = copy.copy(cls.page_dictionary[page_type])
                cls.configure_page(page, web_driver)
                return page
        return None

    @classmethod
    def release_resources(cls):
        if cls.session_driver is not None:
            cls.session_driver.quit()
            cls.session_driver = None
