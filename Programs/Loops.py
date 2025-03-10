# Loops in Python

# For Loop
print("For Loop:")
for i in range(5):
    print("Iteration", i)

# For Loop with List
print("\nFor Loop with List:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# For Loop with Dictionary
print("\nFor Loop with Dictionary:")
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key, ":", person[key])

# While Loop
print("\nWhile Loop:")
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Nested Loops
print("\nNested Loops:")
for i in range(3):
    for j in range(2):
        print("i =", i, ", j =", j)

# Loop Control Statements

# Break Statement
print("\nBreak Statement:")
for i in range(5):
    if i == 3:
        break
    print("Iteration", i)

# Continue Statement
print("\nContinue Statement:")
for i in range(5):
    if i == 3:
        continue
    print("Iteration", i)

# Pass Statement
print("\nPass Statement:")
for i in range(5):
    if i == 3:
        pass  # Do nothing
    print("Iteration", i)