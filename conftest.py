import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


BASE_URL = 'https://b2c.passport.rt.ru/'

@pytest.fixture(scope='module')
def driver():
    service = Service('C:/Users/asvor/OneDrive/Desktop/Unit_29/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver

    driver.quit()
