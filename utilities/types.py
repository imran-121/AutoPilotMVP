from typing import TypeVar, Callable

from appium.webdriver.webdriver import WebDriver
from core.ui.pages.base_page import BasePage
from core.ui.pages.page_type import PageType


PageTypeGeneric = TypeVar("PageTypeGeneric", bound=BasePage)
PageCreatorOld = Callable[[PageType], PageTypeGeneric]

AppiumDriverCreator = Callable[[str], WebDriver]
