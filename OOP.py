# classes in depth
#creating simple class
# class Person:
#     # method (function): you have to provide self as the first argument
#     # self represents the instance of the class

#     def talk(self):
#         print("This is a class")

# #create instance of the class
# person1 = Person()

# #call the method 
# person1.talk()


#The best way to understand self is to realize that a 
# Class is just a blueprint, but an Object is a specific house.

#If you have 100 different people (objects) created from 
# the same Person class, self is the way Python knows
# which specific person is currently talking

#constructors 
# name = "noe"
# class Employee:
#     def __init__(self, name, role, salary):
#         self.name = name
#         self .role = role
#         self.salary = salary
#         print(f"Name : {self.name}")
#         print(f"name :  {name}")

# #instance/object
# employee1 = Employee("Alice", "Manager", 50000)

# employee2 = Employee("Bob", "Developer", 60000)

# print("Employee 1: ", employee1.name, employee1.role, employee1.salary)
# print("Employee 2: ", employee2.name, employee2.role, employee2.salary)

#static variable/Class variable
# belongs to the class itself 
# rather than to any specific instance (object).
# While Instance Variables (using self) are unique 
# to every object you create,
# a Static Variable is shared by all instances of that class.

# class Character:
#     # Every character created will share this same gravity value
#     race = "Human" #static variable
    
#     def __init__(self, name, age):
#         # Every character has their own unique name
#         self.name = name
#         self.age = age


# character1 = Character("Alice", 25)
# character2 = Character("Bob", 30)

# print("Character 1: ", character1.name, character1.age, character1.race)
# print("Character 2: ", character2.name, character2.age, character2.race)


#=======================================================
#OOP
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism
#===========================================================

# Super/ Parent/ Base Class
# class Animal:
#     def __init__(self, animal_name):
#         self.animal_name = animal_name

#     def animal_sound(self):
#         print(f"The animal {self.animal_name} makes a sound")


# # Sub/ Child/ Derived Class
# class Dog(Animal):
#     def bark(self):
#         print(f"The dog {self.animal_name} barks")

# dog1 = Dog("Buddy")
# dog1.animal_sound()
# dog1.bark()

# #Single inheritance: a child class inherits from a single parent class
# #Multiple inheritance: a child class inherits from multiple parent classes

# class Workout:
#     def __init__(self, workout_target_muscles, workout_duration):
#         self.workout_target_muscles = workout_target_muscles
#         self.workout_duration = workout_duration
#         print("Parent Constructor: ")
#         print(f"Workout Target Muscles: {self.workout_target_muscles}")
#         print(f"Workout Duration: {self.workout_duration}")

# class Upper_body(Workout):
#     #overiding the parent constructor
#     def __init__(self, workout_type):
#         self.workout_type = workout_type
#         print("Child Constructor: ")
#         print(f"Workout Type: {self.workout_type}")
#     def my_workout_type(self):
#         print(f"Workout Type==: {self.workout_type}")
    
# upper_body_workout = Upper_body("Pushups")
# print(upper_body_workout.workout_type)
# upper_body_workout.my_workout_type()

# #using super keyword
# class Lower_body(Workout):
#     def __init__(self, workout_target_muscles, workout_duration):
#         super().__init__(workout_target_muscles, workout_duration)
#         print("Child Constructor: ")
#         print(f"Workout Target Muscles: {self.workout_target_muscles}")
#         print(f"Workout Duration: {self.workout_duration}")

# lower_body_workout = Lower_body("Legs", "30 minutes")

#polymorphism
# Polymorphism refers to the ability of objects of
#  different classes to respond to the same method
#  call in different ways.
# 

#Method Over Loading: different methods with 
# the same name but different parameters
# Also called Compile Time Polymorphism/ Static Polymorphism
# class MathOperations:
#     def multiply(self,x,y):
#         return x * y
#     def multiply(self,x,y,z):
#         return x * y * z

# multiply = MathOperations()
# # print(multiply.multiply(2,3)) #error: multiply() missing 1 required positional argument: 'z'
# print(multiply.multiply(2,3,4)) 

# class Cal():
#     def add(self,a,b= None):
#         if b is None:
#             return a
#         else:
#             return a + b

# cal = Cal()
# print(cal.add(2))
# print(cal.add(2,3))

# #Duck Typing
# # Duck typing is a programming technique 
# # where the type of an object is less 
# # important than the methods it provides

# class Dog:
#     def speak(self):
#         print("Woof!")

# class Parrot:
#     def speak(self):
#         print("Squeak!")

# class Duck:
#     def speak(self):
#         print("Quack!")

# class Gorilla:
#     def walk(self):
#         print("Gorilla is walking")

# dog = Dog()
# parrot = Parrot()
# duck = Duck()
# gorilla = Gorilla()

# #function that accepts any object with speak method
# def make_sound(animal):
#     return animal.speak()

# make_sound(dog)
# make_sound(parrot)
# make_sound(duck)
# # make_sound(gorilla) #error: gorilla has no attribute 'speak'


#Encapsulation: Hiding internal details and 
# exposing only the necessary interface

#Public modifier
# class MyClass:
#     def __init__(self,x):
#         #Public attribute
#         self.x = x
#     # public method
#     def get_x(self):
#         return self.x
    
# obj = MyClass(5)
# print(obj.get_x())
# print(obj.x)

#Protected modifier: not intended to be accesed from outside the class 
#but there is no strict enforcement of this
# class MyClass:
#     def __init__(self,x):
#         #protected attribute
#         self._x = x

#     #protected method    
#     def get_x(self):
#         return self._x
    
# obj = MyClass(6)
# print(obj.get_x())
# print(obj._x)


# class MyClass:
#     def __init__(self,x):
#         #private attribute
#         self.__x = x

#     #private method    
#     def get_x(self):
#         return self.__x

# obj = MyClass(7)
# print(obj.get_x())

# #accessing private attribute
# print(obj._MyClass__x) #name mangling

#In Python, when you use a double underscore __, 
# it triggers a process called Name Mangling.
# Python internally renames the variable to 
# _ClassName__VariableName to prevent it 
# from being easily accessed or accidentally 
# overridden by subclasses.


#Encapsulation: Hiding internal details and 
# exposing only the necessary interface

class Person:
    def __init__(self, name,age,gender):
        self._name = name #protected attribute
        self.__age = age #private attribute
        self.__gender = gender #private attribute
        
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age>0:
            self.__age = age
        else:
            print("Age should be greater than 0")
    
    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        if gender in ['M' ,'F', 'Other']:
            self.__gender = gender
        else:
            print("Gender should be M, F, or Other")
    
person = Person("John", 5, "M")
print(person.get_age())
person.set_age(30)
print(person.get_age())

print(person.get_gender())
person.set_gender("F")
print(person.get_gender())

print(person._Person__age)
print(person._Person__gender)

person.set_age(-1)
person.set_gender('A')