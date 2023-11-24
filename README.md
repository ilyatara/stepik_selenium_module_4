Реализация финального задания курса ["Автоматизация тестирования с помощью Selenium и Python"](https://stepik.org/course/575/promo) на платформе [Stepik](https://stepik.org).

Набор UI-автотестов для демо-сайта http://selenium1py.pythonanywhere.com/ с использованием подхода PageObject.

Запуск тестов осуществляется с помощью фреймворка PyTest.

Доступные параметры запуска:
<br>```--browser_name: chrome or firefox (default chrome)```
<br>```--language: en, fr, de, etc. (user language, default en)```


Запуск всех тестов в FireFox с интерфейсом на французском языке:
```
pytest -v --tb=line --browser=firefox --language=fr
```

Запуск тестов с маркером need_review в Chrome на английском языке:
```
pytest -v --tb=line -m need_review
```
