# task3 basic_info
name, age, question = input("Введите ваше имя: "),  int(input("Сколько лет вы работаете в QA? ")), input("Что такое переменная? ")
if age >= 1 and type(name) == str and question == "Переменная это именованная область памяти, которая может менять свое значение":
    print(f"Привет, {name}! Добро пожаловать в мир Python для тестировщиков.")
else:
    print("Мы вам перезвоним")