from .pages import SearchPage, ResultPage


class WebApp:
    def __init__(self, driver, environment_config):
        self.config = environment_config
        self.driver = driver
        self.search_page = SearchPage(self.driver)
        self.result_page = ResultPage(self.driver)

    def shutdown(self):
        self.driver.quit()

    def open_google(self):
        self.driver.get(self.config['google_url'])
        self.search_page.wait()

    def search(self, stuff):
        self.search_page.search(stuff)
        self.result_page.wait()
    
    def get_first_result(self):
        return self.result_page.get_first_result()
