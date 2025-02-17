import time
from conftest import *
from settings import *
from locators import *


'''Восстановление пароля по email'''

def test_forgot_password_by_email(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Забыл пароль"
    driver.find_element(*AuthPage.FORGOT_PASSWORD_BUTTON).click()
    time.sleep(3)

    # Нажать на кнопку "Почта"
    driver.find_element(*AuthPage.EMAIL_TAB).click()
    time.sleep(3)

    # Ввести валидный email
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_email)
    time.sleep(3)

    # Нажать на кнопку "Продолжить"
    driver.find_element(*AuthPage.RESET_FORGOT_PASSWORD_BTN1).click()
    time.sleep(3)

    # Выбрать "Почта"
    driver.find_element(*AuthPage.FORGOT_PASSWORD_BY_EMAIL).click()
    time.sleep(3)

    # Нажать на кнопку "Продолжить"
    driver.find_element(*AuthPage.RESET_FORGOT_PASSWORD_BTN2).click()
    time.sleep(3)

    # Проверка, что код восстановления пароля отправлен на email
    assert driver.find_element(*AuthPage.FORGOT_PASSWORD_TITLE).text == 'Восстановление пароля'


'''Восстановление пароля по телефону'''

def test_forgot_password_by_phone(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Забыл пароль"
    driver.find_element(*AuthPage.FORGOT_PASSWORD_BUTTON).click()
    time.sleep(3)

    # Нажать на кнопку "Телефон"
    driver.find_element(*AuthPage.PHONE_TAB).click()
    time.sleep(3)

    # Ввести валидный телефон
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_phone)
    time.sleep(3)

    # Нажать на кнопку "Продолжить"
    driver.find_element(*AuthPage.RESET_FORGOT_PASSWORD_BTN1).click()
    time.sleep(3)

    # Выбрать "телефон"
    driver.find_element(*AuthPage.FORGOT_PASSWORD_BY_PHONE).click()
    time.sleep(3)

    # Нажать на кнопку "Продолжить"
    driver.find_element(*AuthPage.RESET_FORGOT_PASSWORD_BTN2).click()
    time.sleep(3)

    # Проверка, что код восстановления пароля отправлен на email
    assert driver.find_element(*AuthPage.FORGOT_PASSWORD_TITLE).text == 'Восстановление пароля'


'''Восстановление пароля по логину'''

def test_forgot_password_by_login(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Забыл пароль"
    driver.find_element(*AuthPage.FORGOT_PASSWORD_BUTTON).click()
    time.sleep(3)

    # Нажать на кнопку "Логин"
    driver.find_element(*AuthPage.LOGIN_TAB).click()
    time.sleep(3)

    # Ввести валидный логин
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_login)
    time.sleep(3)

    # Нажать на кнопку "Продолжить"
    driver.find_element(*AuthPage.RESET_FORGOT_PASSWORD_BTN1).click()
    time.sleep(3)

    # Выбрать "почта"
    driver.find_element(*AuthPage.FORGOT_PASSWORD_BY_EMAIL).click()
    time.sleep(3)

    # Нажать на кнопку "Продолжить"
    driver.find_element(*AuthPage.RESET_FORGOT_PASSWORD_BTN2).click()
    time.sleep(3)

    # Проверка, что код восстановления пароля отправлен на email
    assert driver.find_element(*AuthPage.FORGOT_PASSWORD_TITLE).text == 'Восстановление пароля'


'''Восстановление пароля по лицевому счёту'''

def test_forgot_password_by_private_account(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Забыл пароль"
    driver.find_element(*AuthPage.FORGOT_PASSWORD_BUTTON).click()
    time.sleep(3)

    # Нажать на кнопку "Лицевой счёт"
    driver.find_element(*AuthPage.PRIVATE_ACCOUNT_TAB).click()
    time.sleep(3)

    # Ввести валидный лицевой счёт
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_personal_account)
    time.sleep(3)

    # Нажать на кнопку "Продолжить"
    driver.find_element(*AuthPage.RESET_FORGOT_PASSWORD_BTN1).click()
    time.sleep(3)

    # Выбрать "телефон"
    driver.find_element(*AuthPage.FORGOT_PASSWORD_BY_PHONE).click()
    time.sleep(3)

    # Нажать на кнопку "Продолжить"
    driver.find_element(*AuthPage.RESET_FORGOT_PASSWORD_BTN2).click()
    time.sleep(3)

    # Проверка, что код восстановления пароля отправлен на email
    assert driver.find_element(*AuthPage.FORGOT_PASSWORD_TITLE).text == 'Восстановление пароля'