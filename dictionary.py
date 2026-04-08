# #Dictionary:
# #A dictionary is a collection which is unordered, changeable and indexed. 
# # In Python dictionaries are written with curly brackets, 
# # and they have keys and values.
# #Each key is unique and if you try to use a 
# # key that already exists, the old value will be overwritten.

# #Create and print a dictionary:
# netflix_show = {
#     "name": "Stranger Things",
#     "release_year": 2016,
#     "genre": "Science Fiction",
#     "seasons": 4
# }
# print(netflix_show)
# print(type(netflix_show))

# #using the dict constructor to create a dictionary:
# netflix_show = dict(name="Bridgerton", release_year=2020, genre="Romance", seasons=3)
# print(netflix_show)
# print(type(netflix_show))

# #dictionaries are unordered, so the items will not appear in the order they were defined:

# #mixed data types in a dictionary:
# netflix_show = {
#     "name": "The Crown",
#     "release_year": 2016,
#     "genre": "Historical Drama",
#     "seasons": 4,
#     "is_active": True
# }
# print(netflix_show)

# #accessing values in a dictionary using keys:
# print(netflix_show["name"])

# #chnage the value of a key in a dictionary:
# netflix_show["seasons"] = 5
# print(netflix_show)

# #adding a new key-value pair to a dictionary
# netflix_show["cast"] = {"Queen Elizabeth II": "Olivia Colman", "Prince Philip": "Tobias Menzies"}
# print(netflix_show)

# #removing a key-value pair from a dictionary:
# del netflix_show["is_active"]
# print(netflix_show)

# #nested dictionaries:
# rooms = {
#     "living_room": {
#         "furniture": ["sofa", "coffee table"],
#         "color": "beige"
#     },
#     "kitchen": {
#         "appliances": ["fridge", "oven"],
#         "color": "white"
#     },
#     "bedroom": {
#         "bed": "twin",
#         "color": "blue"
#     }
# }
# print(rooms)

#using list of tuples
# stationary =[("pens", "pencils"),("pocketNotes", "stickyNotes"),("erasers", "sharpeners"),("stencils", None),('compasses','rulers')]

# print(stationary)
# print(type(stationary))

# from_tuples_to_dict = dict(stationary)
# print(from_tuples_to_dict)
# print(type(from_tuples_to_dict))

# food = {
#     "fruits": ["apple", "banana", "orange"],
#     "vegetables": ["carrot", "broccoli", "spinach"],
#     "grains": ["rice", "wheat", "oats"]
# }
# # using get method to access values in a dictionary:
# print(food.get("grains"))
# print("get vegetables:", food.get("vegetables"))
# print("get carrot:", food.get("vegetables")[0])

# #iteratinf through a dictionary:
# for category in food:
#     print("Food category:", category)
#     for item in food[category]:
#         print(" -", item)

# drinks = {
#     "hot": ["tea", "coffee", "hot chocolate"],
#     "cold": ["water", "soda", "juice"]
# }
# for drink in drinks:
#     print(f"{drink}: {', '.join(drinks[drink])}")

#iterating through items

# Cities_and_countries = {
#     "New York": "USA",
#     "Paris": "France",
#     "Tokyo": "Japan",
#     "Sydney": "Australia"
# }
# for city, country in Cities_and_countries.items():
#     print(f"{city} is in {country}")