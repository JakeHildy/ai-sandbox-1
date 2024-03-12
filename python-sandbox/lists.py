# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Mixed data types
mixed_list = [1, "Hello", 3.14]

print(fruits[1])

fruits[1] = "blueberry"
print(fruits)

# Using append() to add an item to the end
fruits.append("orange")
print(fruits)

# Using insert() to add an item at a specific position
fruits.insert(0, "banana")
fruits.insert(0, "banana")
print(fruits)

# Removing an item by value
fruits.remove("banana")
print(fruits)

# Removing an item by index and getting its value
popped_fruit = fruits.pop(0)
print(popped_fruit)

del fruits[0]
print(fruits)

# List Comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [number ** 3  for number in numbers]
print(squared_numbers)


randos = ["jake", 4, {"fast": True}, 12]