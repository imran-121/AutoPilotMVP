from selenium import webdriver

'''
    To encapsulate edge browser driver creation
'''


class EdgeBrowser:
    """ To create edge selenium web driver
        Returns:
            Browser: edge WebDriver of chromium browser
    """

    @staticmethod
    def create_web_driver():
        options = webdriver.EdgeOptions()
       
        options.add_argument("--disable-gpu")
        options.add_argument("--start - maximized")
        options.add_argument("--window-size=1280,800")
        options.add_argument("--no-sandbox")
        
        service = webdriver.EdgeService(log_output="./././results/edge_browser.log")
        browser = webdriver.Edge(options=options, service = service )
      
        return browser
