
def calculate_homework(homework_grades):
    total = sum(homework_grades.values())
    average = total / len(homework_grades)
    print('average:', round(average,2))