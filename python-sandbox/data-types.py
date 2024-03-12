# Integer
my_int = 10
# print(my_int)

# Float
my_float = 20.5
# print(my_float)

# String
my_string = "Hello, Python!"
# print(my_string)

# Boolean
my_bool = True
# print(my_bool)

# List
my_list = [1, 2.5, 'Python']
# print(my_list)

# Tuple
my_tuple = (1, 2.5, 'Python')
# print(my_tuple)

# Set
my_set = {1, 2, 3, 2}  # Duplicates will be removed
# print(my_set)

# Dictionary
my_dict = {'name': 'John', 'age': 30}
# print(my_dict)

mixed_data_types = [1, 2.5, "jake", False, ('jake', 'hildebrandt'), {1, 2, 2, 2, 3}, {"name": "jake", "style": "none", "age": 23}]
# print(mixed_data_types)

for data_type in mixed_data_types:
    print(f"{data_type} is of type {type(data_type)}")

