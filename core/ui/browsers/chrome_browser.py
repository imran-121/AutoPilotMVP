from selenium import webdriver

'''
    To encapsulate Chrome browser driver creation
'''


class ChromeBrowser:
    """ To create chrome selenium web driver

        Returns:
            Browser: Selenium WebDriver of Chrome browser
    """

    @staticmethod
    def create_web_driver():
        
        
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-gpu")
        options.add_argument("--start - maximized")
        options.add_argument("--window-size=1280,800")
        
        service = webdriver.ChromeService(log_output="./././results/chrome_browser.log")
        browser = webdriver.Chrome(service = service, options=options)
        return browser
