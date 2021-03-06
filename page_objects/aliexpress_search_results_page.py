from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage


class AliExpressSearchResultsPage(BasePage):

    def pagination_button(self, page_index):
        element_path = ".//div[contains(@class, 'next-pagination-list')]/button[contains(@aria-label, 'Page %s')]" \
            % page_index
        by = By.XPATH

        return BaseElement(driver=self.driver, element_path=element_path, by=by)

    def result_element_sales(self, element_index):
        element_path = ".//div[@product-index=%s]//a[@class='sale-value-link']" % element_index
        by = By.XPATH

        return BaseElement(driver=self.driver, element_path=element_path, by=by)

    @property
    def results_list(self):
        element_path = ".//div[contains(@class, 'list product-card')]"
        by = By.XPATH

        return BaseElement(driver=self.driver, element_path=element_path, by=by)

    @property
    def dialog_popup_close_button(self):
        element_path = ".//a[contains(@class, 'next-dialog-close')]"
        by = By.XPATH

        return BaseElement(driver=self.driver, element_path=element_path, by=by)
