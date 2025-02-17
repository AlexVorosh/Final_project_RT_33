import time
from conftest import *
from settings import *
from locators import *


'''Регистрация с невалидным именем, фамилией'''

def test_reg_invalid_name_lastname(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Войти"
    driver.find_element(*AuthPage.REGISTER_BUTTON).click()
    time.sleep(3)

    # Ввести невалидное имя
    driver.find_element(*RegPage.FIRST_NAME).send_keys(invalid_first_name)
    time.sleep(3)

    # Ввести невалидную фамилию
    driver.find_element(*RegPage.LAST_NAME).send_keys(invalid_last_name)
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

    # Проверка, что высвечиваются ошибки в полях "Имя" и "Фамилия"
    assert driver.find_element(*RegPage.ERROR_NAME_MESSAGE).text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    assert driver.find_element(*RegPage.ERROR_LASTNAME_MESSAGE).text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


'''Регистрация с пустым полем "Регион" и невалидным email'''

def test_reg_invalid_email_empty_region(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Войти"
    driver.find_element(*AuthPage.REGISTER_BUTTON).click()
    time.sleep(3)

    # Ввести валидное имя
    driver.find_element(*RegPage.FIRST_NAME).send_keys(valid_first_name)
    time.sleep(3)

    # Ввести валидную фамилию
    driver.find_element(*RegPage.LAST_NAME).send_keys(valid_last_name)
    time.sleep(3)

    # Ввести невалидный email
    driver.find_element(*RegPage.REG_EMAIL).send_keys(invalid_reg_email)
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

    # Проверка, что высвечиваются ошибки в полях "Имя" и "Фамилия"
    assert driver.find_element(*RegPage.ERROR_REGION_MESSAGE).text == 'Укажите регион'
    assert driver.find_element(*RegPage.ERROR_EMAIL_PHONE_MESSAGE).text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'


'''Регистрация с разными паролями'''

def test_reg_confirm_password_is_different(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Войти"
    driver.find_element(*AuthPage.REGISTER_BUTTON).click()
    time.sleep(3)

    # Ввести валидное имя
    driver.find_element(*RegPage.FIRST_NAME).send_keys(valid_first_name)
    time.sleep(3)

    # Ввести валидную фамилию
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

    # Ввести невалидный пароль (подтверждение)
    driver.find_element(*RegPage.CONFIRM_REG_PASSWORD).send_keys(invalid_conf_reg_password)
    time.sleep(3)

    # Нажать кнопку "Зарегистрироваться"
    driver.find_element(*RegPage.SUBMIT_REGISTRATION_BUTTON).click()
    time.sleep(3)

    # Проверка, что высвечиваются ошибки в полях "Имя" и "Фамилия"
    assert driver.find_element(*RegPage.ERROR_DIFFERENT_PASSWORDS_MESSAGE).text == 'Пароли не совпадают'


'''Регистрация с невалидным паролем'''

def test_reg_invalid_password(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Войти"
    driver.find_element(*AuthPage.REGISTER_BUTTON).click()
    time.sleep(3)

    # Ввести валидное имя
    driver.find_element(*RegPage.FIRST_NAME).send_keys(valid_first_name)
    time.sleep(3)

    # Ввести валидную фамилию
    driver.find_element(*RegPage.LAST_NAME).send_keys(valid_last_name)
    time.sleep(3)

    # Выбрать регион из списка вручную
    driver.find_element(*RegPage.REGION_SELECTION).click()
    time.sleep(10)

    # Ввести валидный email
    driver.find_element(*RegPage.REG_EMAIL).send_keys(valid_reg_email)
    time.sleep(3)

    # Ввести невалидный пароль
    driver.find_element(*RegPage.REG_PASSWORD).send_keys(invalid_reg_password)
    time.sleep(3)

    # Ввести невалидный пароль (подтверждение)
    driver.find_element(*RegPage.CONFIRM_REG_PASSWORD).send_keys(invalid_conf_reg_password)
    time.sleep(3)

    # Нажать кнопку "Зарегистрироваться"
    driver.find_element(*RegPage.SUBMIT_REGISTRATION_BUTTON).click()
    time.sleep(3)

    # Проверка, что высвечиваются ошибки в полях "Имя" и "Фамилия"
    assert driver.find_element(*RegPage.ERROR_INVALID_EMAIL_MESSAGE).text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'


'''Регистрация email который уже зарегистрирован в системе'''

def test_reg_email_already_registered(driver):
    # Перейти на страницу авторизации
    driver.get(BASE_URL)

    # Нажать на кнопку "Войти"
    driver.find_element(*AuthPage.REGISTER_BUTTON).click()
    time.sleep(3)

    # Ввести валидное имя
    driver.find_element(*RegPage.FIRST_NAME).send_keys(valid_first_name)
    time.sleep(3)

    # Ввести валидную фамилию
    driver.find_element(*RegPage.LAST_NAME).send_keys(valid_last_name)
    time.sleep(3)

    # Выбрать регион из списка вручную
    driver.find_element(*RegPage.REGION_SELECTION).click()
    time.sleep(10)

    # Ввести валидный email
    driver.find_element(*RegPage.REG_EMAIL).send_keys(valid_email)
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

    # Проверка, что высвечиваются ошибки в полях "Имя" и "Фамилия"
    assert driver.find_element(*RegPage.USERNAME_EXIST_MESSAGE).text == 'Учётная запись уже существует'

