# Module: file that has python code that can be reused
# Modules can be imported and used in other files
# Python standard library modules provide ready to use functionality

#ways to import
# import module_name : imports complete module
# import module_name as alias : imports complete module with an alias
# from module_name import item_name : imports specific item
# from module_name import item_name as alias_name : imports specific item with an alias
# from  module_name import * : imports all items from the module

#refer file: Math.py
# we can provide an alias "math" because just my_math looks bad
# import my_math
# import my_math as math

# print(math.favorite_number)
# print(math.sum(2,2))
# print(math.multiply(2,2))
# print(math.divide(2,2))
# print(math.subtract(2,2))

#importing a specific thing from module
from my_math import multiply

print(multiply(2,2))

#importing multiple things
from my_math import (sum, divide)

print(sum(20,2))
print(divide(20,2))

#imports specific item with an alias
from my_math import sum as add

print(add(2,2))

#import all items from the module
from my_math import *
print(square(3))