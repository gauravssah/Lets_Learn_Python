s1 = {1,6,0,3,5,7,9}
s2 = {2,4,6,8,10,0,9}

print(s1.union(s2)) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s1.intersection(s2)) # {0, 9, 6}
print(s1.issubset(s2)) # False
print(s1.difference(s2)) # {1, 3, 5, 7}