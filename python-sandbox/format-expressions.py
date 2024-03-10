number = 42
print(f"{number:b}")
print(f"{number:x}")

print(f"{number:.2f}")

percent = 0.25
print(f"{percent:.2%}")

name = "The Tale of the Fisherman and the Fish"
def box_decorator(func):
    def wrapper(text):
        length = len(text) + 4
        print("=" * length)
        print(f"| {text} |")
        print("=" * length)
    return wrapper

@box_decorator
def print_heading(text):
    print(text)

print_heading(name)
