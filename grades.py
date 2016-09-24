#dictionaries of students and their grades
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

#get the average of their specific subject
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total/len(numbers)

#get the students average of all his/her grades
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests
    
#find their grade
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#class average
def get_class_average(students):
    results = []
    for student in students:
        avg = get_average(student)
        results.append(avg)
    return average(results)

print get_letter_grade(get_average(lloyd))
class_avg = get_class_average([lloyd, alice, tyler])
print class_avg
print get_letter_grade(class_avg)
