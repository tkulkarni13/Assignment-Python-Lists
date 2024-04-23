# Task 1:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[7:14])

# Task 2:

above_100_temps = []
for temp in temperatures: # only adds temperatures to list if they are above 100
    if (temp > 100):
        above_100_temps.append(temp)
print(above_100_temps)

# Task 3:

temperatures.reverse()
print(temperatures[-10:-5])
#print(temperatures[5:10])