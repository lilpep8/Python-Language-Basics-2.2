# task5 test_case_stats
tests = int(input('Введите количество тест-кейсов выполненных за неделю '))
medium_tests = (tests // 7)
if medium_tests > 10:
    print(f'{medium_tests} в день в среднем. Отличная работа!')
else:
    print('Попробуйте улучшить свой результат! Иначе придется искать другую работу.')