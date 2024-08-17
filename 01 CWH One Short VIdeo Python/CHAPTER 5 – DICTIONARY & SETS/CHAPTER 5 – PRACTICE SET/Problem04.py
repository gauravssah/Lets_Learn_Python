# 4. What will be the length of following set s:

s= set()
s.add(20)
s.add(20.0)
s.add('20') 

# length of s after these operations?

print(len(s))  # 2 || Why - 20, 20.0 
# Explain - We can have a set with 20 (int), 20.0 (float) and '20' (str) as a value in it.
# Because - Set stores only unique values.

