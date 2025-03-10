# Range Function Examples

# Basic range
basic_range = range(5)
print("Basic range(5):", list(basic_range))

# Range with start and stop
start_stop_range = range(2, 10)
print("Range with start and stop range(2, 10):", list(start_stop_range))

# Range with start, stop, and step
start_stop_step_range = range(1, 10, 2)
print("Range with start, stop, and step range(1, 10, 2):", list(start_stop_step_range))

# Range with negative step
negative_step_range = range(10, 0, -2)
print("Range with negative step range(10, 0, -2):", list(negative_step_range))

# Using range in a for loop
print("Using range in a for loop:")
for i in range(5):
    print(i, end=' ')
print()

# Using range to iterate over a list
sample_list = ['a', 'b', 'c', 'd', 'e']
print("Using range to iterate over a list:")
for i in range(len(sample_list)):
    print("Index", i, ":", sample_list[i])

# Using range to create a list of squares
squares = [x**2 for x in range(1, 11)]
print("List of squares from 1 to 10:", squares)

# Using range to create a list of even numbers
evens = [x for x in range(2, 21, 2)]
print("List of even numbers from 2 to 20:", evens)

# Using range to create a list of odd numbers
odds = [x for x in range(1, 20, 2)]
print("List of odd numbers from 1 to 19:", odds)