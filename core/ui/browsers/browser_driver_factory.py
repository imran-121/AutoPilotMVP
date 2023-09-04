from utilities.logger import Logger
from core.ui.browsers.browser_type import BrowserType
from core.ui.browsers.chrome_browser import ChromeBrowser
from core.ui.browsers.edge_browser import EdgeBrowser
from .head_less_browser import HeadLessBrowser

"""
    BrowserDriverFactory is responsible to build various browser drivers.
    
"""
logger = Logger("browser_driver_factory")


class BrowserDriverFactory:
    """ To create browser objects that encapsulates creation of
            selenium web driver
    Returns:
        Browser: WebDriver of Selenium

    """

    @staticmethod
    def create_web_driver(browser_type: BrowserType):
        logger.debug(f"Creating ${browser_type} browser")
        if browser_type == BrowserType.Chrome:
            return ChromeBrowser.create_web_driver()
        elif browser_type == BrowserType.Edge:
            return EdgeBrowser.create_web_driver()
        else:
            return HeadLessBrowser.create_web_driver()
