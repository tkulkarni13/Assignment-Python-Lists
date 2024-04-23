# import numpy as np

# Task 1:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort() # sort list in ascending order
grades.reverse()
print(grades) # reverse list to get decsending order

# Task 2:

#print(np.mean(grades))
print(sum(grades) / len(grades))

# Task 3:

for i, g in enumerate(grades):
    if (g < 80):
        grades[i] = "Failed"
print(grades)