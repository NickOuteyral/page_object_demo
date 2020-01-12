class AliExpressSearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def pagination_button(self, page_index):
        pass

    def result_element_sales(self, element_index):
        pass