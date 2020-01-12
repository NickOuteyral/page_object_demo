from selenium import webdriver
import unittest

from page_objects.aliexpress_landing_page import AliExpressLandingPage


class TestAliExpress(unittest.TestCase):

    def setUp(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.chrome = webdriver.Chrome('drivers/chromedriver', chrome_options=options)

        self.test_input_value = 'iPhone'

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

    def tearDown(self):

        pass

if __name__ == '__main__':
    unittest.main()
