# Python/Selenium boilerplate
Boiler plate for E2E tests, enforcing PEP8 coding style.

# Prerequisites
Unix-like system with python 3.6.4 and pipenv installed

# Install dependencies
`pipenv install`

# Run tests
`make behave`

# Configure tests
`BROWSER=FIREFOX-LOCAL TEST_ENV=DE make behave`

Default is local Chrome browser and CZ environment, configuration is located at `tests/config.yaml`.
