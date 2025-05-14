# # task8 test_case_validation.py
def check_performance():
    day_tests = int(input())
    if day_tests > 10:
        print( "Отличная работа!")
    elif 10 > day_tests > 0:
        print("Попробуйте улучшить результат.")
    else:
        print("Некорректный ввод. Введите положительное число.")
