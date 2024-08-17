values = {
    "Rahul": 98,
    "Sonia": 97,
    "Sagar": 99,
    "Sachin": 96,
    "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "dict": {
        "a": 1,
        "b": 2
    },
    "set": {1, 2, 3, 4, 5},
    "tuple": (1, 2, 3, 4, 5),
    "string": "Rahul",
    "boolean": True,
    "none": None,
    0 : "Zero",
    1 : "One"
}


print(values.items()) # is's print all keys and values in the form of tuple

# dict_items([('Rahul', 98), ('Sonia', 97), ('Sagar', 99), ('Sachin', 96), ('list', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), ('dict', {'a': 1, 'b': 2}), ('set', {1, 2, 3, 4, 5}), ('tuple', (1, 2, 3, 4, 5)), ('string', 'Rahul'), ('boolean', True), ('none', None), (0, 'Zero'), (1, 'One')])


print(values.keys()) # is's print all keys in the form of list

# dict_keys(['Rahul', 'Sonia', 'Sagar', 'Sachin', 'list', 'dict', 'set', 'tuple', 'string', 'boolean', 'none', 0, 1])


print(values.values()) # is's print all values in the form of list

# dict_values([98, 97, 99, 96, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], {'a': 1, 'b': 2}, {1, 2, 3, 4, 5}, (1, 2, 3, 4, 5), 'Rahul', True, None, 'Zero', 'One'])

print(values) # It's print whole dictionary

# {'Rahul': 98, 'Sonia': 97, 'Sagar': 99, 'Sachin': 96, 'list': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'dict': {'a': 1, 'b': 
# 2}, 'set': {1, 2, 3, 4, 5}, 'tuple': (1, 2, 3, 4, 5), 'string': 'Rahul', 'boolean': True, 'none': None, 0: 'Zero', 1: 'One'}


schoolMarks = {
    "Rahul": 98,
    "Sonia": 97,
    "Sagar": 99,
    "Sachin": 96
}

print(len(schoolMarks)) # 4

schoolMarks.update({"Rahul": 36, "Gaurav": 100}) # It's update the dictionary
print(schoolMarks) 
# {'Rahul': 36, 'Sonia': 97, 'Sagar': 99, 'Sachin': 97, 'Gaurav': 100}

print(schoolMarks.get("Rahul")) # 36
print(schoolMarks["Gaurav"]) # 100




