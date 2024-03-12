# # === Basics === 
# my_tuple = ("apple", "banana", "cherry")
# print(my_tuple)

# item = my_tuple[0]  # Accesses "banana"
# print(item)


# # Tuples are immutable, but you can delete the tuple completely.
# del my_tuple
# # print(my_tuple)  # Raises an error

# # Tuple Methods
# # Tuples have two built-in methods: count() and index().
# # count() returns the number of times a specified value occurs in a tuple.
# # index() searches the tuple for a specified value and returns the position of where it was found.

# my_tuple = ("apple", "banana", "cherry", "apple")
# print(my_tuple.count("apple"))  # Output: 2
# print(my_tuple.index("cherry"))  # Output: 2

# my_second_tuple = (2, "jake", 2.5, True, [1, 2, 3], (1, 2, 3))
# print(my_second_tuple)


# === Example: Data Packing and Unpacking === 
# Function that returns multiple values packed in a tuple
def get_user_info():
    # Imagine fetching user information from a database
    name = "John Doe"
    age = 30
    email = "johndoe@example.com"
    # The function returns these values packed in a tuple
    return name, age, email  # This is tuple packing


# Unpacking the returned tuple into variables
user_name, user_age, user_email = get_user_info()

print(f"Name: {user_name}, Age: {user_age}, Email: {user_email}")


# This feature is particularly elegant for swapping values between 
# two variables without needing a temporary variable:
a = 5
b = 10
# Swap values
a, b = b, a
print(f"a = {a}, b = {b}")  # Output: a = 10, b = 5