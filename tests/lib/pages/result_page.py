from .base_page import BasePage


class ResultPage(BasePage):
    ready_selector = 'div#resultStats'
    result_selector = 'h3.LC20lb'

    def get_first_result(self):
        return self.d.find_element_by_css_selector(self.result_selector).text
