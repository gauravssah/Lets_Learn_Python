# 6. Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = MyClass("Gaurav", 21)
print(obj.name)

obj.name = "Hari"
print(obj.name)














