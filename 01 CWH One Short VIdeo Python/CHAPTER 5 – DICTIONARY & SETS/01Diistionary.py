# Dictionary is a collection of key value pairs
# Dictionary is a collection of non-repetitive elements
# Dictionary is a collection of unique elements
# Dictionary is an unordered collection of elements
# Dictionary is an iterable
# Dictionary is mutable
# Dictionary is not subscriptable
# Dictionary is not indexable
# Dictionary is not hashable
# Dictionary is not iterable
# Dictionary is not JSON serializable
# Dictionary is not JSON deserializable
# Dictionary is not XML serializable

# -----------------------------------------


marks = {
    "Rahul": 98,
    "Sonia": 97,
    "Sagar": 99,
    "Sachin": 96,
    "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

print(type(marks))  # <class 'dict'>
print(marks) # {'Rahul': 98, 'Sonia': 97, 'Sagar': 99, 'Sachin': 96}
print(marks["Rahul"]) # 98
print(marks.get("Rahul")) # 98
print(marks["list"]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(marks.Sonia) # KeyError | AttributeError: 'dict' object has no attribute 'Sonia'

