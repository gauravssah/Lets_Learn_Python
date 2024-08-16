# what is tuple explain
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.


thistuple = ("apple", "banana", "cherry", 55, 5.2, False, "pineapple", 55) # can't change

print(thistuple) # ('apple', 'banana', 'cherry', 55, 5.2, False, 'pineapple')

print(len(thistuple)) # 7

print(type(thistuple)) # <class 'tuple'>


# Tuple methods

print(thistuple.count(55)) # 2
print(thistuple.index("pineapple")) # 6

print(2 in thistuple) # False
print("pineapple" in thistuple) # True

