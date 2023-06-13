# Final task for building test project
## Synopsys
Stepik course Software Testing: Automation and Programming.Python.Selenium

The repository contains final task for building test project from Programming.Python course on Stepik educational platform.

[The link on course](https://stepik.org/course/120491/info)

[The link on task](https://stepik.org/lesson/761692/step/1?unit=763815)


Примечание:

В проекте можно запустить тест для гостя и для зарегистрированного пользователя.
В conftest.py добавлены две опции email и password.
Если при запуске pytest опции не указаны, запустится только тест для гостя.

Для того чтобы запустить тест и для зарегистрированного
пользователя необходимо:
1. Зарегистрировать своего пользователя
2. При запуске pytest указать значения для опций email и password.

Пример:
pytest --email "Ваш email" --password "Ваш password" -v -s ./Tests/test_buy_product.py

