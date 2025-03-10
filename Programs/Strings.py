# String Operations and Methods

# Creating a string
str1 = "Hello"
str2 = "World"

# Concatenation
concat = str1 + " " + str2
print(f"Concatenation: '{str1}' + ' ' + '{str2}' = '{concat}'")

# Repetition
repeat = str1 * 3
print(f"Repetition: '{str1}' * 3 = '{repeat}'")

# Indexing
first_char = str1[0]
print(f"Indexing: The first character of '{str1}' is '{first_char}'")

# Slicing
slice_str = str1[1:4]
print(f"Slicing: str1[1:4] of '{str1}' = '{slice_str}'")

# Length
length = len(str1)
print(f"Length: The length of '{str1}' is {length}")

# String Methods



# Convert to uppercase
upper_str = str1.upper()
print(f"Uppercase: '{str1}'.upper() = '{upper_str}'")

# Convert to lowercase
lower_str = str1.lower()
print(f"Lowercase: '{str1}'.lower() = '{lower_str}'")

# Capitalize the first letter
capitalized_str = str1.capitalize()
print(f"Capitalize: '{str1}'.capitalize() = '{capitalized_str}'")

# Find a substring
find_sub = str1.find('e')
print(f"Find: '{str1}'.find('e') = {find_sub}")

# Replace a substring
replace_str = str1.replace('l', 'p')
print(f"Replace: '{str1}'.replace('l', 'p') = '{replace_str}'")

# Split a string
split_str = concat.split(' ')
print(f"Split: '{concat}'.split(' ') = {split_str}")

# Join a list of strings
join_str = '-'.join(split_str)
print(f"Join: '-'.join({split_str}) = '{join_str}'")

# Check if string starts with a substring
starts_with = str1.startswith('He')
print(f"Startswith: '{str1}'.startswith('He') = {starts_with}")

# Check if string ends with a substring
ends_with = str1.endswith('lo')
print(f"Endswith: '{str1}'.endswith('lo') = {ends_with}")

# Strip whitespace from the beginning and end
str_with_spaces = "  Hello World  "
stripped_str = str_with_spaces.strip()
print(f"Strip: '{str_with_spaces}'.strip() = '{stripped_str}'")