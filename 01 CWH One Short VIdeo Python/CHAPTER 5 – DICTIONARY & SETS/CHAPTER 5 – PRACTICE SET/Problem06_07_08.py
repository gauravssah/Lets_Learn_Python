# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.


d = {}  

for i in range(4):
    name = input("Enter your name: ")
    language = input("Enter your favorite language: ")
    # d[name] = language   # Both ways are correct
    d.update({name : language})

print(type(d)) # <class 'dict'>

# {'Rahul': 'Python', 'Sonia': 'Java', 'Sagar': 'C++', 'Sachin': 'C#'} 

print(d) 

# --------------------------------------

# 7. If the names of 2 friends are same; what will happen to the program in problem 
# 6?


# Enter your name: Gaurav
# Enter your favorite language: java
# Enter your name: Gaurav
# Enter your favorite language: javascript
# Enter your name: sonu
# Enter your favorite language: c++
# Enter your name: mohan
# Enter your favorite language: python

# This will print:   print(d) 

{'Gaurav': 'javascript', 'sonu': 'c++', 'mohan': 'python'}


# ----------------------------------

# 8. If languages of two friends are same; what will happen to the program in problem 
# 6?

# Enter your name: Gaurav
# Enter your favorite language: java
# Enter your name: sonu
# Enter your favorite language: c++
# Enter your name: monu 
# Enter your favorite language: java
# Enter your name: sonu 
# Enter your favorite language: python

# This will print:   print(d) 

{'Gaurav': 'java', 'sonu': 'python', 'monu': 'java'}
