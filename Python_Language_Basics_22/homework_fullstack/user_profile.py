# task4 user_profile
name = input("Введите ваше имя: ")
if not name:
    name = input("Введите ваше имя еще раз: ")


profession = input("Введите кем вы работаете: ")
if not profession:
    profession = input("Введите кем вы работаете имя еще раз: ")


favourite_tool = input("Введите ваш любимый инструмент для тестирования: ")
if not favourite_tool:
    favourite_tool = input("Введите ваш любимый инструмент для тестирования еще раз: ")


if name and profession and favourite_tool:
    print(f'{name} - {profession}, ваш любимый интсрумент: {favourite_tool}. Отличный выбор!')
else:
    print("Вы указали не все данные!")
