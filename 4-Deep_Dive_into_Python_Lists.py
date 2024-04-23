# Task 1:

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for i, g in enumerate(grades):
    if (g < 80):
        print (students[i] + ", " + str(g) + ", " + activities[i])

# Task 2:

students_approved = []
for i, g in enumerate(grades):
    if (g > 80):
        students_approved.append(students[i])

# Task 3:

print(students_approved)