class classExample:
    def __init__(self, name):
        self.name = name
    
    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")
    
    def get_age(self, age):
        return self.age
    
    def set_age(self, age):
        self.age = age

newExample = classExample("Daniel")