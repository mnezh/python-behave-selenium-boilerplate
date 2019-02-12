from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.d = driver

    def wait(self):
        WebDriverWait(self.d, 20).until(
            lambda driver:
                driver
                .find_element_by_css_selector(self.ready_selector))
