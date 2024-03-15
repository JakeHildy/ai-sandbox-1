L = [1, 2, 3]
D = {"jake": 33, "karli": 34}

# it = iter(L)
# dictIt = iter(D)

# print(it.__next__())
# print(next(it))
# print(it.__next__())

# print(next(dictIt))
# print(next(dictIt))
# print(next(dictIt))

# for person in iter(D):
#     print(person)


# t = tuple(iter(L))
# d = tuple(iter(D))
# print(t)
# print(d)

# Sequence unpacking also supports iterators
# a, b, c = iter(L)
# print(a, b, c)


# Thedict()constructorcanacceptaniteratorthatreturnsafinitestreamof(key, value)tuples:
list = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
listDict = dict(iter(list))
print(listDict)