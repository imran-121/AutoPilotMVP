import logging
import time

from core.ui.pages.playground_page import PlayGroundScreen
from core.ui.pages.page_factory import PageFactory
from core.ui.pages.page_type import PageType


class PlaygroundDriver(object):
    """
    Class to excecute the combination of pages, right now we have only one page
    """
    def __init__(self):
        self.playground_page = PageFactory.get_page(PageType.PlayGroundScreen)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.playground_page.visit()
        