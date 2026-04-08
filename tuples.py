# #tuples: tuples are immutable lists. 
# #They cannot be changed after they are created. 
# #They are defined using parentheses ()
# #instead of square brackets [].

# #Example of a tuple
# hobbies = ("reading", "coding", "hiking", "cooking")
# print(hobbies)
# #Accessing elements in a tuple
# print(hobbies[0])
# print(hobbies[2])

# #Tuples can also contain different data types
# person = ("Alice", 30, "Engineer", True)
# print(person)
# print(type(person[2]))
# print(type(person[3]))

# #Tuples can be used to store related data 
# #that should not be changed,
# #such as coordinates or RGB color values.
# coordinates = (10.5, 20.3)
# print("Coordinates:", coordinates)

# #assigning values to a tuple
# colors = ('red', 'green', 'blue')
# # colors[1] = 'yellow' #This will raise an error because tuples are immutable

# #add new elements to a tuple by concatenating it with another tuple
# new_colors = colors + ('yellow',)
# print(new_colors)

# #weird tuple things
# nums = 1, 2, 3
# print(type(nums)) #This will print <class 'tuple'> because the parentheses are optional when defining a tuple with multiple elements

# #single element tuple
# single_tuple = (5,)
# print(type(single_tuple)) #This will print <class 'tuple'> because the comma is necessary to indicate that it is a tuple, otherwise it would be just an integer.

# #iterating through a tuple
# for hobby in hobbies:
#     print(hobby)
    
