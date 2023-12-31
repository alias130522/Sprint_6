import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def driver():
    firefox_options = Options()
    firefox_options.set_headless()
    driver = webdriver.Firefox(options=firefox_options)

    yield driver
    driver.quit()

