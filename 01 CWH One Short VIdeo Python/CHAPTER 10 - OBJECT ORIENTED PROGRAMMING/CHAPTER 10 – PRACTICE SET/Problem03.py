# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class MyClass:
    a = 10

obj = MyClass()
print(obj.a)  # This will print 10

obj.a = 0  # This will not change the class attribute, its just create a object insted and print it 

print(obj.a)  # This will print 0

print(MyClass.a)  # This will print 10








