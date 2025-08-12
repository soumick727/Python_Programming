# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# .keys() - returns all keys
print(my_dict.keys())  # dict_keys(['a', 'b', 'c'])

# .values() - returns all values
print(my_dict.values())  # dict_values([1, 2, 3])

# .items() - returns all key-value pairs
print(my_dict.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# .get(key, default) - gets value for key, returns default if not found
print(my_dict.get('b'))        # 2
print(my_dict.get('z', 0))     # 0

# .update() - updates dictionary with another dictionary
my_dict.update({'d': 4})
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# .pop(key, default) - removes key and returns its value
value = my_dict.pop('a')
print(value)    # 1
print(my_dict)  # {'b': 2, 'c': 3, 'd': 4}

# .clear() - removes all items
my_dict.clear()
print(my_dict)  # {}

print(type(my_dict))  # <class 'dict'>