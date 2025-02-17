import time
from conftest import *
from settings import *
from locators import *


'''Позитивный тест - авторизация по номеру телефона'''

def test_phone_authorization(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Выбрать вкладку "Телефон"
    driver.find_element(*AuthPage.PHONE_TAB).click()

    # Ввести номер мобильного телефона
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_phone)
    time.sleep(3)

    # Ввести действующий пароль
    driver.find_element(*AuthPage.PASSWORD).send_keys(valid_password)
    time.sleep(3)

    # Нажать кнопку "Войти"
    driver.find_element(*AuthPage.SUBMIT_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(*AuthPage.PRIVATE_ACCOUNT_CABINET).text == 'Личный кабинет'
    time.sleep(3)

    # Нажать кнопку "Выйти"
    driver.find_element(*AuthPage.LOGOUT_BUTTON).click()
    time.sleep(3)


'''Позитивный тест - авторизация по email'''

def test_email_authorization(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Выбрать вкладку "Почта"
    driver.find_element(*AuthPage.EMAIL_TAB).click()

    # Ввести почту
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_email)
    time.sleep(3)

    # Ввести пароль
    driver.find_element(*AuthPage.PASSWORD).send_keys(valid_password)
    time.sleep(3)

    # Нажать кнопку "Войти"
    driver.find_element(*AuthPage.SUBMIT_BUTTON).click()
    time.sleep(3)

    # Проверка, что авторизация прошла успешно
    assert driver.find_element(*AuthPage.PRIVATE_ACCOUNT_CABINET).text == 'Личный кабинет'

    # Нажать кнопку "Выйти"
    driver.find_element(*AuthPage.LOGOUT_BUTTON).click()
    time.sleep(3)


'''Позитивный тест - авторизация по логину'''

def test_login_authorization(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Выбрать вкладку "Логин"
    driver.find_element(*AuthPage.LOGIN_TAB).click()

    # Ввести логин
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_login)
    time.sleep(3)

    # Ввести пароль
    driver.find_element(*AuthPage.PASSWORD).send_keys(valid_password)
    time.sleep(3)

    # Нажать кнопку "Войти"
    driver.find_element(*AuthPage.SUBMIT_BUTTON).click()
    time.sleep(3)

    # Проверка, что авторизация прошла успешно
    assert driver.find_element(*AuthPage.PRIVATE_ACCOUNT_CABINET).text == 'Личный кабинет'

    # Нажать кнопку "Выйти"
    driver.find_element(*AuthPage.LOGOUT_BUTTON).click()
    time.sleep(3)


'''Позитивный тест - авторизация по лицевому счету'''

def test_login_personal_account(driver):
    driver.get(BASE_URL)

    # Выбрать вкладку "Лицевой счет"
    driver.find_element(*AuthPage.PRIVATE_ACCOUNT_TAB).click()

    # Ввести лицевой счет
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_personal_account)
    time.sleep(3)

    # Ввести пароль
    driver.find_element(*AuthPage.PASSWORD).send_keys(valid_password)
    time.sleep(3)

    # Нажать кнопку "Войти"
    driver.find_element(*AuthPage.SUBMIT_BUTTON).click()
    time.sleep(3)

    # Проверка, что авторизация прошла успешно
    assert driver.find_element(*AuthPage.PRIVATE_ACCOUNT_CABINET).text == 'Личный кабинет'
    time.sleep(3)

    # Нажать кнопку "Выйти"
    driver.find_element(*AuthPage.LOGOUT_BUTTON).click()
    time.sleep(3)