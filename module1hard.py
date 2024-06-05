grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_of_students = sorted(students)
print(list_of_students)
average_grades = {}
# Расчет 1-го ученика
sum_of_nums = sum(grades[0])
count = len(grades[0])
average_grades[0] = sum_of_nums / count
print(average_grades[0])
# Расчет 2-го ученика
sum_of_nums = sum(grades[1])
count = len(grades[1])
average_grades[2] = sum_of_nums / count
print(average_grades[2])
# Расчет 3-го ученика
sum_of_nums = sum(grades[2])
count = len(grades[2])
average_grades[3] = sum_of_nums / count
print(average_grades[3])
# Расчет 4-го ученика
sum_of_nums = sum(grades[3])
count = len(grades[3])
average_grades[4] = sum_of_nums / count
print(average_grades[4])
# Расчет 5-го ученика
sum_of_nums = sum(grades[4])
count = len(grades[4])
average_grades[5] = sum_of_nums / count
print(average_grades[5])
print(average_grades)
# Создаем словарь
result = {}
result.update({list_of_students[0]}: average_grades[0]) # Почему выдает синтаксическую ошибку?
print(result)
