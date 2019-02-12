from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    input_selector = 'input.gsfi'
    submit_selector = 'input[name="btnK"]'
    ready_selector = input_selector

    def search(self, stuff):
        self.d.find_element_by_css_selector(
          self.input_selector).send_keys(stuff)
        WebDriverWait(self.d, 10).until(
          EC.element_to_be_clickable(
            (By.CSS_SELECTOR, self.submit_selector)))
        self.d.find_element_by_css_selector(self.submit_selector).click()
