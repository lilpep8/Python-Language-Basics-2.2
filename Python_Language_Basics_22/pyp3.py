# Коллекции данных задачи:

# task 1
numbers = [1,2,3]
numbers.append(4)
print(numbers)

# task2
fruits = ["Москва", "Лондон", "Париж"]
fruits.remove("Лондон")
print(fruits)

# task3
cities = ["Москва","Питер","Новосибирск","Екатеринбург"]
print(cities[2])

# task4
numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers[3:7])

# task5
colors = ["red","green","blue"]
colors[1] = "yellow"
print(colors)

# task6
animals = ["cat", "dog", "rabbit", "hamster"]
print(len(animals))

# task7
student = {"name": "Ivan", "age":20}
student["grade"] = "A"
print(student)

# task8
student = {'name': 'Ivan', 'age': 20, 'grade': 'B'}
student['grade'] = 'A'
print(student)

# task9
student = {'name': 'Ivan', 'age': 20, 'grade': 'A'}
del student['age']
print(student)

# task10
student = {'name': 'Ivan', 'age': 20, 'grade': 'A'}
print(student['name'])

# task11
student = {'name': 'Ivan', 'age': 20, 'grade': 'A'}
print('grade' in student)
print('color' in student)

# task12
python_copy_edit_student = {"name": "Ivan", "address":{"city":"Moscow", "street": "Lenina"}}
python_copy_edit_student["address"]["city"] = "Saint Petesburg"
print(python_copy_edit_student)

# task13
python_copy_edit_student = {"name":"Maria", "grades":[75,82,90]}
python_copy_edit_student["grades"][0] = 85
print(python_copy_edit_student)

# task14
python_copy_edit_student = [{"name":"Ivan","age":20}, {"name":"Petya","age":22}]
python_copy_edit_student[1]["age"] = 23
print(python_copy_edit_student)

# task15
CopyEditColors = ("red", "green","blue")
print(len(CopyEditColors), "green" in CopyEditColors)