# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")
        
class Pet(Animal):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        print(f"{self.name} is playing.")

class Dog(Pet):
    @staticmethod
    def bark():
        print(f"Dog is barking.")   
        
 
myDog = Dog("Rex")
myDog.eat()
myDog.sleep()
myDog.play()
myDog.bark()

