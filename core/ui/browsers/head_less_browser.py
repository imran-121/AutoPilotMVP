from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
    To encapsulate Headless browser driver creation
'''


class HeadLessBrowser:
    """ To create Headless selenium web driver

        Returns:
                Browser: Selenium web driver of Headless browser

    """
    @staticmethod
    def create_web_driver():
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-gpu')
        options.add_argument("--window-size=1920,1080")

        service = webdriver.ChromeService(log_output="./././results/chrome_browser.log")
        browser = webdriver.Chrome(service = service, options=options)
        
        return browser
