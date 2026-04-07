# print("Hello World")
# this is a comment
# variables
# age =30
# print(age)
# age = 10
# print(age)

# arithmetic operations
# sum_result = 6+6
# print("SUM:",sum_result)
# difference_result = 6-6
# print("DIFFERENCE:",difference_result)
# product_result = 6*6
# print("PRODUCT:",product_result)
# quotient_result = 6/6
# print("QUOTIENT:",quotient_result)
# power_result = 6**6
# print("POWER:",power_result)
# modulus_result = 6%6
# print("MODULUS:",modulus_result)

# rounded_result = 30//2
# print("ROUNDED:",rounded_result)


# Inputs
# name = input("What is your name? ")
# print("Hello", name)

#assignment operators
# x= 5
# x+=3 # x= x+3
# print(x)
# x-=3 # x= x-3
# print(x)
# x*=3 # x= x*3
# print(x)
# x/=3 # x= x/3
# print(x)
# x%=3 # x= x%3
# print(x)
# x**=3 # x= x**3
# print(x)
# x//=3 # x= x//3
# print(x)

# strings

# single_line_string = "This is a single line string"
# multi_line_string = """This is a multi 
# line string that can span
# multiple lines without the need for escape characters."""
# print(single_line_string)
# print()
# print(multi_line_string)

# string concatenation
# first_name = "John"
# last_name = "Doe"
# full_name = first_name + " " + last_name
# print("Full Name:", full_name)
# print(len(full_name))


# String indexing and slicing
# text = "Hello, World!"
# first_character = text[0]
# print("First Character:", first_character)
# last_character = text[-1]
# print("Last Character:", last_character)
# substring = text[7:10]
# print("Substring:", substring)

# String formatting
# name = "Alice"
# age = 25
# message = f"My name is {name} and I am {age} years old."
# print(message)
# formatted_message = f"2+2={2+2}"
# print(formatted_message)


# Escape characters
# text_with_newline = "Hello,\nWorld!"
# print(text_with_newline)
# text_with_tab = "Hello,\tWorld!"
# print(text_with_tab)
# text_with_quotes = "She said, \"Hello!\" "
# print(text_with_quotes)
# text_with_backslash = "C:\\path\\to\\file"
# print(text_with_backslash)

#booleans
# x = True
# y = False
# location = "New York"
# number = 42
# another_number = 3.14
 

# print(type(x))
# print(type(location))
# print(type(number))
# print(type(another_number))

#TypeCasting: converting one data type to another
# number_as_string = str(number)
# print(type(number_as_string))
# print(number_as_string)
# string_as_number = int("44")
# print(type(string_as_number))
# print(string_as_number)
# float_as_string = str(another_number)
# print(type(float_as_string))
# print(float_as_string)
# string_as_float = float("4.25")
# print(type(string_as_float))
# print(string_as_float)
# float_as_int = int(another_number)
# print(type(float_as_int))
# print(float_as_int)
# int_as_float = float(number)
# print(type(int_as_float))
# print(int_as_float)


#String methods
# new_string = "This is a sample string for demonstrating string methods."
# print(new_string.upper())
# print(new_string.lower())
# print(new_string.title())
# print(new_string.capitalize())
# print(new_string.replace("sample", "example"))
# print(new_string.find("for"))
# print(new_string.startswith("This"))
# print(new_string.endswith("method."))
# print("================")
# new_string = "   This is a sample string for demonstrating string methods.   "
# print(new_string.split(" "))
# print(new_string.strip()) # Remove leading and trailing whitespace characters.
# print(new_string.lstrip()) # Remove leading whitespace characters.
# print(new_string.rstrip()) # Remove trailing whitespace characters.

# print(new_string.count("s")) # Count the number of occurrences of the substring "s" in the string. This will count both uppercase and lowercase "s" characters.
# print(new_string.isalpha()) # Every character is a letter (A-Z). No numbers, spaces, or symbols.
# print(new_string.isdigit()) # Every character is a digit (0-9). No letters, spaces, or symbols.
# print(new_string.isalnum()) # Every character is either a letter or a digit. No spaces or symbols.
# print(new_string.islower()) # Every character is a lowercase letter (a-z). No uppercase letters, spaces, or symbols.
# print(new_string.isupper()) # Every character is an uppercase letter (A-Z). No lowercase letters, spaces, or symbols.
# print(new_string.istitle()) # Every word starts with an uppercase letter followed by lowercase letters. No numbers, spaces, or symbols.
# print(new_string.swapcase()) #Every character is a letter (A-Z). No numbers, spaces, or symbols.

#Comparison operators
# a = 10
# b = 20
# print("a:", a)
# print("b:", b)

# print("is a equal to b?",a == b) # Equal to
# print("is a not equal to b?",a != b) # Not equal to
# print("is a greater than b?",a > b) # Greater than
# print("is a less than b?",a < b) # Less than
# print("is a greater than or equal to b?",a >= b) # Greater than or equal to
# print("is a less than or equal to b?",a <= b) # Less than or equal to
# print("is a the same object as b?",a is b) # Identity operator: checks if a and b refer to the same object in memory.
# print("is a not the same object as b?",a is not b) # Identity operator: checks if a and b do not refer to

#Logical operators
g = True
h = False

print("g:", g)
print("h:", h)

print("g and h:", g and h) # Logical AND: True if both g and h are True, otherwise False.
print("g or h:", g or h) # Logical OR: True if at least one
print("not g:", not g) # Logical NOT: True if g is False, and False if g is True.
print("not h:", not h) # Logical NOT: True if h is False, and False if h is True.