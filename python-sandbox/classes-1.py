class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def feed_dog(self):
        self.is_hungry = False

    def __str__(self):
        return f'{self.name} is {self.age} years old'


class Bulldog(Dog):  # Inherits from Dog
    def run(self, speed):
        return f"{self.name} runs {speed}"


# nova = Dog('Nova', 3)
# print(nova.is_hungry)
# nova.feed_dog()
# print(nova.is_hungry)
# print(nova)

henry = Bulldog('Henry', 5)
print(henry)
print(henry.run('fast'))
