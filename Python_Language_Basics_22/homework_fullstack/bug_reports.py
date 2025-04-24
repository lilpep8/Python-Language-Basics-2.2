# task6 bug_reports
bugs = ["Ошибка 1 — High", "Ошибка 2 — High", "Ошибка 3 — medium", "Ошибка 4 — Low", "Ошибка 5 — Low"]
bugs.append("Ошибка 6 - High")
bugs.remove("Ошибка 4 — Low")
bugs.remove("Ошибка 5 — Low")


sorted_bugs = sorted(bugs, key=lambda x: "High" in x)
print(sorted_bugs[::-1])