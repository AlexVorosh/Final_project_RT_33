# Дипломный проект: реальный кейс компании «Ростелеком Информационные Технологии» 

Тестируемый сайт: https://b2c.passport.rt.ru/

При тестировании сайты были разработаны:

 - Тест-кейсы

- Автоматизированные тесты

- Составлены баг-репорты

При тестировании сайта были применены следующие техники тест-дизайна:

- Техника разбиения на классы эквивалентности и анализ граничных значений – создание тестовых данных для ввода в поля формы регистрации нового пользователя: имя, фамилия, email, номер телефона, пароль.
- Попарное тестирование (pairwise testing) — тестирование формы регистрации (проверяются все возможные комбинации каждой пары входных параметров).  
- Техника исследовательского тестирования (на основании пользовательского опыта) – описание/название элементов форм (табы, слоганы, надписи, кнопки, поля ввода), расположение элементов, авторизация в системе. 

При тестировании сайта были использованы инструменты:

- https://texttools.ru/random-string-generator — генератор случайных строк — помощь в создании строк нужной длины и набора символов

- https://text.ru/seo — подсчет символов в тексте — применялось для тестирования граничных значений для ввода в поля формы регистрации нового пользователя: имя, фамилия, email, номер телефона, пароль.

- Плагин для Chrome XPath Helper – помощь в редактированиии и поиск XPath локатора на веб-странице


Структура проекта:

- Папка tests содержит следующие файлы: 
  - test_auth_negative.py –  негативные тесты страницы авторизации; 
  - test_auth_positive.py –  позитивные тесты страницы авторизации; 
  - test_forgot_password.py – позитивные тесты страницы восстановления пароля; 
  - test_reg_negative.py - негативные тесты страницы регистрации; 
  - test_reg_positive.py - позитивные тесты страницы регистрации; 
  - test_tab_switching.py – автоматическое переключение вкладок на странице авторизации

Также проект содержит такие файлы, как: 

  - conftest.py – фикстуры для работы с браузером 
  - locators.py – список всех локаторов
  - settings.py – список валидных и невалидных данных для тестирования 

Для запуска автотестов необходимо вводить команды в консоли терминала. 

Для позитивных тестов страницы регистрации: 

 - python -m pytest -v --driver Chrome --driver-path ‪<chromedriver_directory>\<chromedriver_file   
 tests\test_reg_positive.py

Для негативных тестов страницы регистрации:

 - python -m pytest -v --driver Chrome --driver-path ‪<chromedriver_directory>\<chromedriver_file>
 tests\test_reg_negative.py

Для позитивных тестов страницы авторизации:

 - python -m pytest -v --driver Chrome --driver-path ‪<chromedriver_directory>\<chromedriver_file>
 tests\test_auth_positive.py

Для негативных тестов страницы авторизации:

 - python -m pytest -v --driver Chrome --driver-path ‪<chromedriver_directory>\<chromedriver_file>
 tests\test_auth_negative.py

Для позитивных тестов восстановления пароля:

  - python -m pytest -v --driver Chrome --driver-path ‪<chromedriver_directory>\<chromedriver_file>
 tests\test_forgot_password.py

Для тестов автоматического переключения вкладок на странице авторизации:

  - python -m pytest -v --driver Chrome --driver-path ‪<chromedriver_directory>\<chromedriver_file>
 tests\test_tab_switching.py

<chromedriver_directory><chromedriver_file> - путь к директории файла драйвера\название файла браузера. Например: C:\Chrome-selenium\chromedriver.exe
