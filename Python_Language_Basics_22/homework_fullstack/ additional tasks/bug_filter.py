# # # task9 bug_filter
tests = ["Ошибка 1 – High",
        "Ошибка 2 – High",
        "Ошибка 3 – Medium",
        "Ошибка 4 – High",
        "Ошибка 5 – Medium",
        "Ошибка 6 – Low",
        "Ошибка 7 – Low",]
answer = []
value = input("Введите приоритет для поиска (High, Medium, Low): ")
for i in tests:
    if value in i:
        i = f"- {i}"
        answer.append(i)
for i in answer:
    print(i)