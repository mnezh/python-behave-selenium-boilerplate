import os
from selenium import webdriver


def get_driver(config):
    local_browsers = {
      'Firefox': webdriver.Firefox,
      'Chrome': webdriver.Chrome
    }
    browser_name = os.environ.get('BROWSER', 'CHROME-LOCAL')
    browser_config = config['browsers'][browser_name]
    # remote selenium support should go there:
    if browser_config['type'] == 'local':
        driver_class = local_browsers[browser_config['browser']]
        if driver_class:
            return driver_class()
    raise RuntimeError('Unknown browser type')
