class Pet: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")
    
class Cat(Pet):
        def __init__(self, name, age, color):
            self.color = color
        
        def speak(self):
            print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")


