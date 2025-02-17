import time
from conftest import *
from settings import *
from locators import *


'''Вкладки "Телефон", "Почта", "Логин", "Лицевой счет" присутствуют на странице авторизации'''

def test_tabs_present(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на вкладку "Телефон"
    driver.find_element(*AuthPage.PHONE_TAB).click()
    time.sleep(3)

    # Проверка, что происходит переключение на вкладку "Телефон"
    assert driver.find_element(*AuthPage.PHONE_FIELD).text == 'Мобильный телефон'

    # Нажать на вкладку "Почта'
    driver.find_element(*AuthPage.EMAIL_TAB).click()
    time.sleep(3)

    # Проверка, что происходит переключение на вкладку "Телефон"
    assert driver.find_element(*AuthPage.EMAIL_FIELD).text == 'Электронная почта'

    # Нажать на вкладку "Логин'
    driver.find_element(*AuthPage.LOGIN_TAB).click()
    time.sleep(3)

    # Проверка, что происходит переключение на вкладку "Логин"
    assert driver.find_element(*AuthPage.LOGIN_FIELD).text == 'Логин'

    # Нажать на вкладку "Лицевой счёт"
    driver.find_element(*AuthPage.PRIVATE_ACCOUNT_TAB).click()
    time.sleep(3)

    # Проверка, что происходит переключение на вкладку "Лицевой счёт"
    assert driver.find_element(*AuthPage.PRIVATE_ACCOUNT_FIELD).text == 'Лицевой счёт'


'''Автоматическое переключение на вкладку "Телефон"'''

def test_phone_tab_switching(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Ввести телефон
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_phone)
    time.sleep(3)

    # Нажать на поле пароль
    driver.find_element(*AuthPage.PASSWORD).click()
    time.sleep(3)

    # Проверка, что происходит переключение на вкладку "Телефон"
    assert driver.find_element(*AuthPage.PHONE_FIELD).text == 'Мобильный телефон'


'''Автоматическое переключение на вкладку "Почта"'''

def test_email_tab_switching(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Ввести email
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_email)
    time.sleep(3)

    # Нажать на поле пароль
    driver.find_element(*AuthPage.PASSWORD).click()
    time.sleep(3)

    # Проверка, что происходит переключение на вкладку "Телефон"
    assert driver.find_element(*AuthPage.EMAIL_FIELD).text == 'Электронная почта'


'''Автоматическое переключение на вкладку "Логин"'''

def test_login_tab_switching(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Ввести логин
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_login)
    time.sleep(3)

    # Нажать на поле пароль
    driver.find_element(*AuthPage.PASSWORD).click()
    time.sleep(3)

    # Проверка, что происходит переключение на вкладку "Телефон"
    assert driver.find_element(*AuthPage.LOGIN_FIELD).text == 'Логин'


'''Автоматическое переключение на вкладку "Лицевой счёт"'''

def test_personal_account_tab_switching(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Почта" чтобы при вводе лицевого счета произошел авто переход на вкладку "Лицевой счёт"
    driver.find_element(*AuthPage.EMAIL_TAB).click()
    time.sleep(3)

    # Ввести лицевой счёт
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_personal_account)
    time.sleep(3)

    # Нажать на поле пароль
    driver.find_element(*AuthPage.PASSWORD).click()
    time.sleep(3)

    # Проверка, что происходит переключение на вкладку "Лицевой счёт"
    assert driver.find_element(*AuthPage.PRIVATE_ACCOUNT_FIELD).text == 'Лицевой счёт'