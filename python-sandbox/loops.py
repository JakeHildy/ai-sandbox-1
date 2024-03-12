# For Loops
# A for loop is used for iterating over a sequence (that is, a list, a tuple, a dictionary, a set, or a string).

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)


# While Loops
# A while loop executes a set of statements as long as a condition is true.
# i = 1
# while i < 6:
#     print(i)
#     i += 1

# Break and Continue
# break is used to exit a loop.
# continue skips the current iteration and continues with the next one.



# Practical Challenge
# Let's combine what we've learned into a practical challenge. Imagine you're 
# working with a list of numbers and you need to find the sum of all even numbers 
# until you reach a number that is greater than 10. If you encounter a number greater 
# than 10, stop the loop.

numbers = [2, 4, 6, 8, 11, 3, 5]

sum = 0
for number in numbers:
    if number > 10:
        break
    if number % 2 == 0:
        sum += number

print(sum)

