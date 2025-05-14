# task6 bug_reports
bugs = ["Ошибка 1 — High", "Ошибка 2 — High", "Ошибка 3 — medium",
        "Ошибка 4 — Low", "Ошибка 5 — Low", "Ошибка 6 - High"]


bugs.remove("Ошибка 4 — Low")
bugs.remove("Ошибка 5 — Low")


def get_priority(bug):
    if "High" in bug:
        return 0
    elif "medium" in bug:
        return 1
    elif "Low" in bug:
        return 2
    return None

sorted_bugs = sorted(bugs, key=get_priority)
print(sorted_bugs)