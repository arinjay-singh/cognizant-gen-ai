# types of exceptions

# IndexError: this occurs when trying to access an index that does not exist in a list
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # invalid index
except IndexError as e:
    print("Caught an IndexError:", e)

# KeyError: this occurs when trying to access a key that does not exist in a dictionary
try:
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])  # non-existent key
except KeyError as e:
    print("Caught a KeyError:", e)

# TypeError: this occurs when performing an operation on incompatible types
try:
    result = 'number: ' + 5  # can't add string and integer
except TypeError as e:
    print("Caught a TypeError:", e)