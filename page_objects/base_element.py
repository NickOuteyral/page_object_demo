from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):

    def __init__(self, driver, element_path, by):
        self.driver = driver
        self.element_path = element_path
        self.by = by

        self.locator = (self.by, self.element_path)

        self.web_element = None
        self.find()

    def find(self):
        self.web_element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator=self.locator))
        return None
    
    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def send_keys(self, query):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        element.clear()
        element.send_keys(query)
        return None

    def text(self):
        text = self.web_element.text
        return text