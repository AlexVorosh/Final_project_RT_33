import time
from conftest import *
from settings import *
from locators import *


'''Позитивный тест - Регистрация - email'''

def test_email_registration(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Зарегистрироваться"
    driver.find_element(*AuthPage.REGISTER_BUTTON).click()

    # Ввести имя
    driver.find_element(*RegPage.FIRST_NAME).send_keys(valid_first_name)
    time.sleep(3)

    # Ввести фамилию
    driver.find_element(*RegPage.LAST_NAME).send_keys(valid_last_name)
    time.sleep(3)

    # Выбрать регион из списка вручную
    driver.find_element(*RegPage.REGION_SELECTION).click()
    time.sleep(10)

    # Ввести валидный email
    driver.find_element(*RegPage.REG_EMAIL).send_keys(valid_reg_email)
    time.sleep(3)

    # Ввести валидный пароль
    driver.find_element(*RegPage.REG_PASSWORD).send_keys(valid_reg_password)
    time.sleep(3)

    # Ввести валидный пароль (подтверждение)
    driver.find_element(*RegPage.CONFIRM_REG_PASSWORD).send_keys(valid_conf_reg_password)
    time.sleep(3)

    # Нажать кнопку "Зарегистрироваться"
    driver.find_element(*RegPage.SUBMIT_REGISTRATION_BUTTON).click()
    time.sleep(3)

    # Проверка, что осуществляется переход на страницу подтверждения email
    assert driver.find_element(*RegPage.CONFIRM_EMAIL_TITLE).text == 'Подтверждение email'


'''Позитивный тест - Регистрация - телефон'''

def test_phone_registration(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Зарегистрироваться"
    driver.find_element(*AuthPage.REGISTER_BUTTON).click()

    # Ввести имя
    driver.find_element(*RegPage.FIRST_NAME).send_keys(valid_first_name)
    time.sleep(3)

    # Ввести фамилию
    driver.find_element(*RegPage.LAST_NAME).send_keys(valid_last_name)
    time.sleep(3)

    # Выбрать регион из списка вручную
    driver.find_element(*RegPage.REGION_SELECTION).click()
    time.sleep(10)

    # Ввести валидный телефон
    driver.find_element(*RegPage.REG_PHONE).send_keys(valid_reg_phone)
    time.sleep(3)

    # Ввести валидный пароль
    driver.find_element(*RegPage.REG_PASSWORD).send_keys(valid_reg_password)
    time.sleep(3)

    # Ввести валидный пароль (подтверждение)
    driver.find_element(*RegPage.CONFIRM_REG_PASSWORD).send_keys(valid_conf_reg_password)
    time.sleep(3)

    # Нажать кнопку "Зарегистрироваться"
    driver.find_element(*RegPage.SUBMIT_REGISTRATION_BUTTON).click()
    time.sleep(3)

    # Проверка, что осуществляется переход на страницу подтверждения телефона
    assert driver.find_element(*RegPage.CONFIRM_PHONE_TITLE).text == 'Подтверждение телефона'
