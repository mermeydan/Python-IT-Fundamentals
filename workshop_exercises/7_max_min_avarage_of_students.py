'''Her öğrencinin ortalamsını bulacağız ve hangi öğrencini en yüksek ortalamya sahip olduğu ve 
hangi öğrencinin en düşük ortalamaya sahip olduğunu bulunuz. (Lamda kullanmayı deneyin)'''

students = {'Student-1': {'Lesson-1': 57, 'Lesson-2': 46, 'Lesson-3': 58, 'Lesson-4': 81, 'Lesson-5': 85}, \
'Student-2': {'Lesson-1': 85, 'Lesson-2': 56, 'Lesson-3': 51, 'Lesson-4': 69, 'Lesson-5': 67}, \
'Student-3': {'Lesson-1': 68, 'Lesson-2': 76, 'Lesson-3': 87, 'Lesson-4': 57, 'Lesson-5': 56}, \
'Student-4': {'Lesson-1': 78, 'Lesson-2': 93, 'Lesson-3': 88, 'Lesson-4': 38, 'Lesson-5': 54}, \
'Student-5': {'Lesson-1': 50, 'Lesson-2': 46, 'Lesson-3': 78, 'Lesson-4': 81, 'Lesson-5': 75}}
def avr_grade(students):  
    avarage_grades = dict(map(lambda x : (x, sum(students[x].values())/ len(students[x].values())), students))
    print(avarage_grades)
    max_grade = max(avarage_grades, key = lambda i: avarage_grades[i])
    min_grade = min(avarage_grades, key = lambda i: avarage_grades[i])
    
    return f"\n{max_grade} has maximum average with a score {avarage_grades[max_grade]}\n{min_grade} has minimum average with a score {avarage_grades[min_grade]}"

print(avr_grade(students))