# # # task9 bug_filter
tests = ["Ошибка 1 – High",
        "Ошибка 2 – High",
        "Ошибка 3 – Medium",
        "Ошибка 4 – High",
        "Ошибка 5 – Medium",
        "Ошибка 6 – Low",
        "Ошибка 7 – Low"]

answer = []
value = input("Введите приоритет для поиска (High, Medium, Low): ")

for test in tests:
    if value in test:
        formatted_test  = f"- {test}"
        answer.append(formatted_test)

for item in answer:
    print(item)