# Task 1:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
part_of_both = []

for name in submitted: # adds name from both lists to a blank list
    if name in attended:
        part_of_both.append(name)

print(part_of_both)

# Task 2:

if (set(submitted) == set(attended)): # convert lists to sets to handle repeats, then compare
    print("Both lists are the same")
else:
    print("Both lists are different")

# Task 3:

for name in attended: # removes names from attended based on if they show up in submitted
    if (name not in submitted):
        attended.remove(name)
print(attended)