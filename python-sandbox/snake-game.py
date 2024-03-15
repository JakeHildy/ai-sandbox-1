import math
# print('--------- SNAKE ----------')
# print('|                        |')
# print('|                        |')
# print('|                        |')
# print('|                        |')
# print('|                        |')
# print('|                        |')
# print('|                        |')
# print('|                        |')
# print('--------------------------')

class Map:
    def __init__(self, size):
        self.size = size
        self.title = "SNAKE"

    def render(self):
       title_length = self.title.__len__() + 2
       remaining = math.ceil((self.size - title_length) / 2)
       top_line = '-' * remaining
       print(f"{top_line} {self.title} {top_line}")


       spaces = ' ' * (self.size - 2)
       empty_line = f"|{spaces}|"
       empty_block = f"{empty_line}\n" * math.floor(self.size / 3)
       print(empty_block)

       

        


map = Map(31)
map.render()


# while True:
#      userInput = input(">> ")
#      print(userInput)