from selenium import webdriver
import unittest

from page_objects.aliexpress_landing_page import AliExpressLandingPage
from page_objects.aliexpress_search_results_page import AliExpressSearchResultsPage


class TestAliExpress(unittest.TestCase):

    def setUp(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.chrome = webdriver.Chrome('drivers/chromedriver', chrome_options=options)

        self.test_input_value = 'iPhone'
        self.element_index = 1
        self.page_index = 2

    def test_elements_sold(self):

        landing = AliExpressLandingPage(driver=self.chrome)
        landing.go()

        try:
            landing.dialog_popup_close_button.click()
        except:
            pass

        landing.search_input.click()
        landing.search_input.send_keys(self.test_input_value)
        landing.submit_button.click()

        search_results = AliExpressSearchResultsPage(driver=self.chrome)

        search_results.results_list.find()
        search_results.scroll_to_bottom()

        try:
            search_results.dialog_popup_close_button.click()
        except:
            pass

        search_results.pagination_button(self.page_index).click()
        search_results_list = search_results.results_list.several()
        assert len(search_results_list) > 1

        items_sold = search_results.result_element_sales(self.element_index).text().split(' ')
        items_sold_int = int(items_sold[0])
        assert items_sold_int > 0, 'result in index %s does not have any sales' % self.element_index

    def tearDown(self):
        self.chrome.quit()


if __name__ == '__main__':
    unittest.main()
