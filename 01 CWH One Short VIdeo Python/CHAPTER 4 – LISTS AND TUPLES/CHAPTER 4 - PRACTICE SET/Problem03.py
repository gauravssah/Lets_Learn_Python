# 3. Check that a tuple type cannot be changed in python.

a = (1, 2, 3, "sah", 5.2)


a[2] = "Gaurav"  # Error : Can't change because it is immutable
