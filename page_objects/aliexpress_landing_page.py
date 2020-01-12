from selenium.webdriver.common.by import By

from base_element import BaseElement
from base_page import BasePage


class AliExpressLandingPage(BasePage):

    url = 'https://www.aliexpress.com/'

    def search_input(self):
        element_path = 'search-key'
        by = By.ID

        return BaseElement(driver=self.driver, element_path=element_path, by=by)

    def submit_button(self):
        element_path = ".//div[contains(@class, 'searchbar-operate-box')]/input"
        by = By.XPATH

        return BaseElement(driver=self.driver, element_path=element_path, by=by)
