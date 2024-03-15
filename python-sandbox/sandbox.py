# john = {
#     "name": "John Doe",
#     "age": 30
# }

# def name_changer(person):
#     person['name'] = "Jake"


# print(john)
# name_changer(john)
# print(john)

# ======== 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

john = Person("John Doe", 30)

def name_changer(person):
    person.name = "Jake"


print(john)
name_changer(john)
print(john)
