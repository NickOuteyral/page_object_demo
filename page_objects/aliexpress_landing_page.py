class AliExpressLandingPage:

    url = 'https://www.aliexpress.com/'

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def search_input(self):
        pass

    def submit_button(self):
        pass