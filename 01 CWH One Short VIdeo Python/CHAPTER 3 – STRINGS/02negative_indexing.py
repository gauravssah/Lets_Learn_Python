name = "Gaurav Sah"

print(name) # Gaurav Sah
print(name[0]) # G
print(name[1]) # a
print(name[2]) # u


print(name[-5:-1]) # v Sa
# same as 
print(name[1:5]) # aura
print(name[-1:-5]) # not possible
print(name[-1]) # h

print(name[:5]) # Gaura ( is same as name[0:5])
print(name[5:]) # v Sah ( is same as name[5:10])

# Slicing with skip value
print(name[0:10:3]) # Gr h

num = [1,2,3,4,5,6,7,8,9,10]
print(num[0:10:2])  # [1, 3, 5, 7, 9]