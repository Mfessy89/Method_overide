#creating the class adult
class Adult():
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour
    
    def can_drive(self):
        print(self.name, "can drive")
#creating the subclass child
class Child(Adult):
    def can_drive(self):
        print(self.name, "is too young to drive")
#asking for user inputs
name = input("Enter name: ")
age = int(input("Enter age: "))
eye_colour = input("Enter eye colour: ")
hair_colour = input("Enter hair colour: ")

if (age >= 18):
    obj = Adult(name, age, eye_colour, hair_colour)
else:
    obj = Child(name, age, eye_colour, hair_colour)

obj.can_drive()
