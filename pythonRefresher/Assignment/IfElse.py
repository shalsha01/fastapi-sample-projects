"""- Create a variable grade holding an integer between 0 - 100
- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:
A = 90 - 100
B = 80 - 89
C = 70-79
D = 60 - 69
F = 0 - 59
Example:
if grade = 87 then print('B')
"""

grade = int(input("Enter your grade: "))

if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade >= 70 and grade <= 79:
    print("C")
elif grade >= 60 and grade <= 69:
    print("D")
elif grade >= 0 and grade <= 49:
    print("F")
else:
    print("Invalid grade entered. Please enter a grade between 0 and 100.")



## or we can wright it like this:
""" if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
elif grade >= 0:
    print("F")  
else:

    print("Invalid grade entered. Please enter a grade between 0 and 100.")

 """