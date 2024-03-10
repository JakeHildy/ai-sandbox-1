class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def __str__(self):
        return self.name



class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"




animals = [Dog("Max"), Cat("Felix")]

# print(animals)
# print(animals[0])

for animal in animals:
    print(animal)


# nova = Dog('Nova')
# print(nova.speak())

# bella = Cat('Bella')
# print(bella.speak())

