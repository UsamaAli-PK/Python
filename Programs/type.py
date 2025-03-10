import typing
# Define a variable of type str
z: str = "Hello, world!"
 
# Define a variable of type int
x: int = 10
# Define a variable of type float
y: float = 1.23
# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]
# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}

# Print the variables
print(z)
print(x)
print(y)
print(list_of_numbers)
print(tuple_of_numbers)
print(dictionary)
print(set_of_numbers)

# Define a function to calculate the area of a triangle
def area_triangle(base, height):
    return base*height/2

area_b = area_triangle(7,3)
print(area_b)
area_a = area_triangle(5,7)
print(area_a)

# Define a function to convert seconds to hours, minutes, and seconds
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
 
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# Define a function to find the total number of days in a given number of years, months, and days
def find_total_days(years, months, days):
    my_days = (years*365) + (months*30) + days
    return my_days

a = find_total_days(2,5,23)

print(a)
