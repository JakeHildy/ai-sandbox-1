from contextlib import contextmanager

@contextmanager
def managed_file(filename):
    try:
        file = open(filename, 'r')
        yield file
    finally:
        file.close()

with managed_file('example.txt') as file:
    contents = file.read()
