# # Functions

# # Registering a function
# def crunchyroll():
#     print("Hello from crunchyroll!")


# # Calling the function
# crunchyroll()

# #function with parameters
# def add_numbers(num1,num2):
#     result = num1 + num2
#     print("The result is:", result)

# # Calling the function with arguments
# add_numbers(2,2)

# #default parameters
# def greet(name = "Guest"):
#     print("Hello", name)

# greet("Tom")
# greet() # will use the default parameter value "Guest"

# def message(headcount = 10):
#     return f"This is a message from the function for {headcount} people"

# print(message()) # will use the default parameter value 10
# print(message(20)) # will use the provided argument value 20

# #named arguments
# def movie_screening(movie_name, time):
#     print("The movie", movie_name, "will be screened at", time)

# movie_screening(movie_name="100 Meters", time="7:00 PM")

# def calculate_bmi(weight,height):
#     bmi = weight / (height ** 2)
#     return bmi

# print(calculate_bmi(70, 1.75))

# def add_and_subtract(num1, num2):
#     sum_result = num1 + num2
#     difference_result = num1 - num2
#     return sum_result, difference_result

# sum_result, difference_result = add_and_subtract(2,2)
# print("Sum", sum_result)
# print("Difference", difference_result)


# #nested functions 
# def anime(name):
#     def browse(genre):
#         return name +" :"+ genre
#     watch = browse("fantasy")
#     return watch

# print(anime("Witch Hat Atelier"))

#lambda functions:
# small anonymous function desfined using lambda keyword
# often reffered to as "lambda expression" 
# lambda functions are used when you need a simple function for short time period
# and do not want to formallt define a full function using the def keyword

# add = lambda x, y : x+y
# print(add(2,2))

# #function that takes another function as argument
# def calculate(x,y,operation):
#     return operation(x,y)

# result_add = calculate(2,3,add)
# print(result_add)

# result_product = calculate(2,3, lambda x,y : x*y)
# print(result_product)

# Scope:
# Refers to the region of a program where a particular variable is accessible.
# Python follows the LEGB rule (Local, Enclosing, Global, Built-in).

#global variable 
# global_variable  = 10

# def local_function():
#     local_variable = 20
#     print("print local variable inside local function:", local_variable )
#     print('print global variable inside local function:', global_variable)

#local scope : variable defined in function is only accessible inside function i.e. they have local scope
#once function is executed local variable is destroyed
# local_function()
# print('print global variable outside function:', global_variable)

#nested scopes : when a fucntion say function_outer is defined in another function say function_inner,
#inner function can access the variables of outer function 
# but outer function cannot access inner function variables

def func_outer():
    outer_variable = 30
    print('print outer variable inside outer function:', outer_variable)
    # print('print inner variable inside outer function:', inner_variable) 
    #Error : above line gives error "inner_variable" is not defined
    def func_inner():
        inner_variable = 40
        print('print inner variable inside inner function:', inner_variable)
        print('print outer variable inside inner function:', outer_variable)
    func_inner()
func_outer()

# ==========================================================
# SCOPE RESOLUTION: THE LEGB RULE
# ==========================================================
# Python looks for variables in this specific order:
#
# 1. LOCAL (L):    Inside the current function.
# 2. ENCLOSING (E): Inside parent functions (Nested/Closures).
# 3. GLOBAL (G):   Top-level of the script (.py file).
# 4. BUILT-IN (B): Python's pre-installed names (print, len, etc.).
#
# Rule: "Inside can see Out, but Outside cannot see In."
# ==========================================================

# def func_outer():
#     # (E) Enclosing Scope
#     x = "Outer" 

#     def func_inner():
#         # (L) Local Scope
#         x = "Inner"
#         print(x) # Found in Local first

#     func_inner()

# # (G) Global Scope
# x = "Global"