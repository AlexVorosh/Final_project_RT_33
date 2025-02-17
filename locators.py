from selenium.webdriver.common.by import By

"""Локаторы для страницы авторизации"""

class AuthPage:

    PHONE_TAB = (By.ID, 't-btn-tab-phone') # Кнопка "Телефон"
    EMAIL_TAB = (By.ID,  't-btn-tab-mail') # Кнопка "Почта"
    LOGIN_TAB = (By.ID, 't-btn-tab-login') # Кнопка "Логин"
    PRIVATE_ACCOUNT_TAB = (By.ID, 't-btn-tab-ls') # Кнопка "Лицевой счёт"
    USERNAME = (By.ID, 'username') # Поле "Мобильный телефон", "Электронная почта", "Логин", "Лицевой счёт"
    PASSWORD = (By.ID, 'password') # Поле "Пароль"
    SUBMIT_BUTTON = (By.ID, 'kc-login') # Кнопка "Войти"
    LOGOUT_BUTTON = (By.ID, 'logout-btn') # Кнопка "Выйти"
    FORGOT_PASSWORD_BUTTON = (By.ID, 'forgot_password') # Кнопка "Забыл пароль"
    RESET_FORGOT_PASSWORD_BTN1 = (By.ID, 'reset') # Кнопка "Продолжить" восстановление пароля
    RESET_FORGOT_PASSWORD_BTN2 = (By.ID, 'reset-form-submit') # Кнопка "Продолжить" восстановления пароля после выбора способа (телефон, почта)
    FORGOT_PASSWORD_TITLE = (By.ID, 'card-title') # Надпись "Восстановление пароля"
    REGISTER_BUTTON = (By.ID, 'kc-register') # Кнопка "Зарегистрироваться"
    T_BANK = (By.ID, 'oidc_tinkoff') # Кнопка "Т-Банк"
    YANDEX = (By.ID, 'oidc_ya') # Кнопка "Yandex"
    VK = (By.ID, 'oidc_vk') # Кнопка "VK"
    MAIL_RU = (By.ID, 'oidc_mail') # Кнопка "MAIL RU"
    OK = (By.ID, 'oidc_ok') # Кнопка "OK"
    PRIVATE_ACCOUNT_CABINET = (By.XPATH, '//*[@id="id_app_lk_b2c"]/div[2]/span') # "Личный кабинет" надпись при авторизации в личном кабинете
    PHONE_FIELD = (By.XPATH, '//span[contains(text(),"Мобильный телефон")]') # Placeholder "Мобильный телефон"
    EMAIL_FIELD = (By.XPATH, '//span[contains(text(),"Электронная почта")]') # Placeholder "Электронная почта"
    LOGIN_FIELD = (By.XPATH, '//span[contains(text(),"Логин")]') # Placeholder "Логин"
    PRIVATE_ACCOUNT_FIELD = (By.XPATH, '//span[contains(text(),"Лицевой счёт")]') # Placeholder "Лицевой счёт"
    PHONE_ERROR_MESSAGE = (By.ID, 'username-meta') # Ошибка при вводе телефона "Введите номер телефона"
    EMAIL_ERROR_MESSAGE = (By.ID, 'username-meta') # Ошибка при вводе email "Введите адрес, указанный при регистрации"
    LOGIN_ERROR_MESSAGE = (By.ID, 'username-meta') # Ошибка при вводе логина "Введите логин, указанный при регистрации"
    PRIVATE_AC_ERROR_MESSAGE = (By.ID, 'username-meta') # Ошибка при вводе лицевого счёта "Введите номер вашего лицевого счета"
    LOGIN_PASSWORD_ER_MESSAGE = (By.ID, 'form-error-message') # Ошибка при вводе неверного логина или пароля "Неверный логин или пароль"
    FORGOT_PASSWORD_BY_PHONE = (By.XPATH, '//*[@id="sms-reset-type"]/span/span[1]') # Выбрать телефон для отправки кода для восстановления пароля
    FORGOT_PASSWORD_BY_EMAIL= (By.XPATH, '//*[@id="email-reset-type"]/span/span[1]') # Выбрать почта для отправки кода для восстановления пароля

"""Локаторы для страницы регистрация"""

class RegPage:

    FIRST_NAME = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input') # Поле "Имя"
    LAST_NAME =  (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input') # Поле "Фамилия"
    REGION = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input') # Поле "Регион"
    REGION_SELECTION = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/div[2]') # Развернуть поле "Регион"
    REG_EMAIL = (By.ID, 'address') # Поле "Email или мобильный телефон"
    REG_PHONE = (By.ID, 'address') # Поле "Email или мобильный телефон"
    REG_PASSWORD = (By.ID, 'password') # Поле "Пароль"
    CONFIRM_REG_PASSWORD = (By.ID, 'password-confirm') # Поле "Подтверждение пароля"
    SUBMIT_REGISTRATION_BUTTON = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button') # Кнопка "Зарегистрироваться"
    CONFIRM_EMAIL_TITLE = (By.XPATH, '//*[@id="page-right"]/div/div/h1') # Надпись "Подтверждение "Email" при регистрации
    CONFIRM_PHONE_TITLE = (By.XPATH, '//*[@id="page-right"]/div/div/h1') # Надпись "Подтверждение телефона" при регистрации
    ERROR_NAME_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span') # Ошибка в поле "Имя"
    ERROR_LASTNAME_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span') # Ошибка в поле "Фамилия"
    ERROR_REGION_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/span') # Ошибка в поле "Регион"
    ERROR_EMAIL_PHONE_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span') # Ошибка некорректный телефон или email
    ERROR_DIFFERENT_PASSWORDS_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/span') # Ошибка "Пароли не совпадают"
    ERROR_INVALID_EMAIL_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span') # Ошибка некорректный пароль"
    USERNAME_EXIST_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/div/h2') # pop-up сообщение "Учётная запись уже существует"




