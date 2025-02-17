import time
from conftest import *
from settings import *
from locators import *


'''Выводится ошибка при авторизации с пустым значением "Телефон""'''

def test_empy_phone_field_message(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Телефон"
    driver.find_element(*AuthPage.PHONE_TAB).click()
    time.sleep(3)

    # Ввести пароль
    driver.find_element(*AuthPage.PASSWORD).send_keys(valid_password)
    time.sleep(3)

    # Нажать на кнопку "Войти"
    driver.find_element(*AuthPage.SUBMIT_BUTTON).click()
    time.sleep(3)

    # Высвечивается ошибка "Введите номер телефона"
    assert driver.find_element(*AuthPage.PHONE_ERROR_MESSAGE).text == 'Введите номер телефона'


'''Выводится ошибка при авторизации с пустым значением "Почта""'''

def test_empy_email_field_message(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Почта"
    driver.find_element(*AuthPage.EMAIL_TAB).click()
    time.sleep(3)

    # Ввести пароль
    driver.find_element(*AuthPage.PASSWORD).send_keys(valid_password)
    time.sleep(3)

    # Нажать на кнопку "Войти"
    driver.find_element(*AuthPage.SUBMIT_BUTTON).click()
    time.sleep(3)

    # Высвечивается ошибка "Введите адрес, указанный при регистрации"
    assert driver.find_element(*AuthPage.EMAIL_ERROR_MESSAGE).text == 'Введите адрес, указанный при регистрации'


'''Выводится ошибка при авторизации с пустым значением "Логин""'''

def test_empy_login_field_message(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Логин"
    driver.find_element(*AuthPage.LOGIN_TAB).click()
    time.sleep(3)

    # Ввести пароль
    driver.find_element(*AuthPage.PASSWORD).send_keys(valid_password)
    time.sleep(3)

    # Нажать на кнопку "Войти"
    driver.find_element(*AuthPage.SUBMIT_BUTTON).click()
    time.sleep(3)

    # Высвечивается ошибка "Введите логин, указанный при регистрации"
    assert driver.find_element(*AuthPage.LOGIN_ERROR_MESSAGE).text == 'Введите логин, указанный при регистрации'


'''Выводится ошибка при авторизации с пустым значением "Лицевой счёт""'''

def test_empy_private_ac_field_message(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Лицевой счёт"
    driver.find_element(*AuthPage.PRIVATE_ACCOUNT_TAB).click()
    time.sleep(3)

    # Ввести пароль
    driver.find_element(*AuthPage.PASSWORD).send_keys(valid_password)
    time.sleep(3)

    # Нажать на кнопку "Войти"
    driver.find_element(*AuthPage.SUBMIT_BUTTON).click()
    time.sleep(3)

    # Высвечивается ошибка "Введите номер вашего лицевого счета"
    assert driver.find_element(*AuthPage.PRIVATE_AC_ERROR_MESSAGE).text == 'Введите номер вашего лицевого счета'


'''Выводится ошибка при авторизации с валидным телефоном и невалидным паролем'''

def test_valid_phone_invalid_pass(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Телефон"
    driver.find_element(*AuthPage.PHONE_TAB).click()
    time.sleep(3)

    # Ввести валидный телефон
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_phone)
    time.sleep(3)

    # Ввести невалидный пароль
    driver.find_element(*AuthPage.PASSWORD).send_keys(invalid_password)

    # Нажать на "Войти"
    driver.find_element(*AuthPage.SUBMIT_BUTTON).click()
    time.sleep(3)

    # Высвечивается ошибка "Неверный логин или пароль"
    assert driver.find_element(*AuthPage.LOGIN_PASSWORD_ER_MESSAGE).text == 'Неверный логин или пароль'


'''Выводится ошибка при авторизации с валидным email и невалидным паролем'''

def test_valid_email_invalid_pass(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Почта"
    driver.find_element(*AuthPage.EMAIL_TAB).click()
    time.sleep(3)

    # Ввести валидный Email
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_email)
    time.sleep(3)

    # Ввести невалидный пароль
    driver.find_element(*AuthPage.PASSWORD).send_keys(invalid_password)

    # Нажать на "Войти"
    driver.find_element(*AuthPage.SUBMIT_BUTTON).click()
    time.sleep(3)

    # Высвечивается ошибка "Неверный логин или пароль"
    assert driver.find_element(*AuthPage.LOGIN_PASSWORD_ER_MESSAGE).text == 'Неверный логин или пароль'


'''Выводится ошибка при авторизации с валидным логином и невалидным паролем'''

def test_valid_login_invalid_pass(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Почта"
    driver.find_element(*AuthPage.LOGIN_TAB).click()
    time.sleep(3)

    # Ввести валидный логин
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_login)
    time.sleep(3)

    # Ввести невалидный пароль
    driver.find_element(*AuthPage.PASSWORD).send_keys(invalid_password)

    # Нажать на "Войти"
    driver.find_element(*AuthPage.SUBMIT_BUTTON).click()
    time.sleep(3)

    # Высвечивается ошибка "Неверный логин или пароль"
    assert driver.find_element(*AuthPage.LOGIN_PASSWORD_ER_MESSAGE).text == 'Неверный логин или пароль'


'''Выводится ошибка при авторизации с валидным лицевым счетом и невалидным паролем'''

def test_valid_private_ac_invalid_pass(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Лицевой счёт"
    driver.find_element(*AuthPage.PRIVATE_ACCOUNT_TAB).click()
    time.sleep(3)

    # Ввести валидный лицевой счёт
    driver.find_element(*AuthPage.USERNAME).send_keys(valid_personal_account)
    time.sleep(3)

    # Ввести невалидный пароль
    driver.find_element(*AuthPage.PASSWORD).send_keys(invalid_password)

    # Нажать на "Войти"
    driver.find_element(*AuthPage.SUBMIT_BUTTON).click()
    time.sleep(3)

    # Высвечивается ошибка "Неверный логин или пароль"
    assert driver.find_element(*AuthPage.LOGIN_PASSWORD_ER_MESSAGE).text == 'Неверный логин или пароль'




