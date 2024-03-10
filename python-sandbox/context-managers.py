with open('example.txt', 'r') as file:
    contents = file.read()
# File is automatically closed here, outside of the block


class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('example.txt') as f:
    print(f.read())

