import os
import threading

import pytest

from utilities.logger import Logger
from utilities.types import PageCreatorOld
from core.ui.pages.page_factory import PageFactory
from core.ui.pages.page_type import PageType

logger = Logger(os.path.basename(__file__))


@pytest.fixture(scope='session')
def page_retriever(ui_base_url, current_browser_type) -> PageCreatorOld:
    """
    Session scope fixture to return function handler, that function
    handler is used to retrieve the page for a given page type.
    :return: function
    """

    def get_page(page_type):
        logger.debug("From conftest::get_page")
        page = PageFactory.get_page(page_type)
        thread_local = threading.current_thread()
        logger.debug("Before setting test_page")

        logger.debug(f" identity from get_page in page_retriever=> {threading.get_ident()}")
        setattr(thread_local, 'test_page', page)
        logger.debug("Before setting test_page")
        logger.debug(threading.get_ident())
        page = getattr(thread_local, 'test_page', None)

        if page is None:
            logger.debug("************************** page attribute is none in get_page  ************************** ")
        return page

    logger.debug("From conftest::page_retriever, before init_resources")
    PageFactory.init_resources(base_url=ui_base_url, browser_type=current_browser_type)
    yield get_page
    logger.debug("with in conftest::page_retriever, release_resources")
    PageFactory.release_resources()


@pytest.fixture(scope='session')
def session_playground_page(page_retriever):
    """
    Session scope fixture to construct the Lock screen page using the given function parameter (page_retriever).
    :param page_retriever:
    :return: LockScreenPage
    """
    logger.debug('within kiosk_lock_screen_page, before page_builder')
    playground_page = page_retriever(PageType.PlayGroundScreen)
    logger.debug("within kiosk_lock_screen_page, before kiosk_lock_screen visit")
    playground_page.visit()
    return playground_page







