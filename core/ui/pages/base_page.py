
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select
from utilities.logger import Logger


class BasePage:
    """######################
    ##### CORE METHODS ########
    ######################"""

    def __init__(self, driver, base_url):
        """To initialize the _driver and URL
        :param driver:
        :param base_url:
        """
        self.URL = base_url
        self._driver = driver
        self._logger = Logger(self.__class__.__name__)
        self.wait_time = 5

    def set_driver(self, driver):
        self._driver = driver

    def get_driver(self):
        return self._driver

    def visit(self):
        """ To go to the URL that has been constructed in initializer method """
        self._logger.debug(f"Url to visit => {self.URL}")
        self._driver.get(self.URL)
        self._driver.maximize_window()
        
    def set_text(self, locator, value):
        """
        Clears the text if it's a text entry locator and Simulates typing into the locator
        :param : locator
        :param :A string for typing, or setting form fields.  For setting
              file inputs, this could be a local file path.
        """

        try:
            target_element = self._driver.find_element(*locator)
            target_element.clear()
            target_element.send_keys(value)
        except NoSuchElementException:
            assert False, f" The locator {locator} not found to perform send keys action"
            
            
    def find_element_and_click(self, locator):
        try:
            target_element = self._driver.find_element(*locator)
            target_element.click()
        except NoSuchElementException:
            assert False, f" The locator {locator} not found to perform send keys action"
            
    def select_option_from_dropdown(self, locator, option_value):
        """
        Selects an option from a dropdown list.
        Args:
            driver: The Selenium WebDriver instance.
            locator: The locator of the dropdown element (XPath, CSS selector, etc.).
            option_value: The value of the option to select.

        Returns:
            None
        """
        try:
            dropdown = self._driver.find_element(*locator)
            select = Select(dropdown)
            select.select_by_value(option_value)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            
            
    def upload_file(self, locator, file_path):
        try:
            target_element = self._driver.find_element(*locator)
            target_element.send_keys(file_path)
        except NoSuchElementException:
            assert False, f" The locator {locator} not found to perform send keys action"

  
