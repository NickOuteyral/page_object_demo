from selenium import webdriver
import unittest

from page_objects.aliexpress_landing_page import AliExpressLandingPage


class TestAliExpress(unittest.TestCase):

    def setUp(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.chrome = webdriver.Chrome('drivers/chromedriver', chrome_options=options)

    def test_elements_sold(self):

        pass

    def tearDown(self):

        pass

if __name__ == '__main__':
    unittest.main()
