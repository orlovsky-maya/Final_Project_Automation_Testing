# Final Project Automation Testing

The repository contains the solution of the final test task.

[Task](https://stepik.org/lesson/761692/step/1?unit=763815)

"Automation Testing" course on Stepik educational platform.

[Course](https://stepik.org/course/120491/info)

## Website under test:

[Website](https://орешкофф.рф/)


<p align="center">
    <img src="https://raw.githubusercontent.com/orlovsky-maya/Final_Project_Automation_Testing/main/Images/Website_1.png" alt="Website_1" height="400" width="800">

</p>

<p align="center">
    <img src="https://raw.githubusercontent.com/orlovsky-maya/Final_Project_Automation_Testing/main/Images/Website_2.png" alt="Website_2" height="400" width="800">

</p>


## Results of run:

<p align="center">
    <img src="https://raw.githubusercontent.com/orlovsky-maya/Final_Project_Automation_Testing/main/Images/Running_Tests.png" 
alt="Running_Tests" height="400" width="950">

</p>



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

