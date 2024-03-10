# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello = my_decorator(say_hello)

# say_hello()


# Decorating Functions With Arguments
# If the function you're decorating takes arguments, you can capture 
# them in the wrapper by using *args and **kwargs:
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         result = func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#         return result
#     return wrapper

# @my_decorator
# def say_something(word):
#     print(word)

# say_something("Hello")


# Practical Use Case: Timing Function Execution
# A common use for decorators is timing how long a function takes to execute:
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time-start_time} seconds to run.")
        return result
    return wrapper

@timer
def long_running_function():
    time.sleep(2)

long_running_function()

