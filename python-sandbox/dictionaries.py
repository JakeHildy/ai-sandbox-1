# A dictionary with a tuple as a key
my_dict = {('John', 'Doe'): 'john.doe@example.com', ('Jane', 'Doe'): 'jane.doe@example.com'}
print(my_dict)

# Accessing the value with a tuple key
print(my_dict[('John', 'Doe')])  # Output: john.doe@example.com

# Adding a new entry with a tuple as a key
my_dict[('Mike', 'Smith')] = 'mike.smith@example.com'
print(my_dict)

