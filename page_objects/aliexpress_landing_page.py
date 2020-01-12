from selenium.webdriver.common.by import By

from base_element import BaseElement


class AliExpressLandingPage:

    url = 'https://www.aliexpress.com/'

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def search_input(self):
        element_path = 'search-key'
        by = By.ID

        return BaseElement(driver=self.driver, element_path=element_path, by=by)

    def submit_button(self):
        element_path = ".//div[contains(@class, 'searchbar-operate-box')]/input"
        by = By.XPATH

        return BaseElement(driver=self.driver, element_path=element_path, by=by)
