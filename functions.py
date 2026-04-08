# Functions

# Registering a function
def crunchyroll():
    print("Hello from crunchyroll!")


# Calling the function
crunchyroll()

#function with parameters
def add_numbers(num1,num2):
    result = num1 + num2
    print("The result is:", result)

# Calling the function with arguments
add_numbers(2,2)

#default parameters
def greet(name = "Guest"):
    print("Hello", name)

greet("Tom")
greet() # will use the default parameter value "Guest"

def message(headcount = 10):
    return f"This is a message from the function for {headcount} people"

print(message()) # will use the default parameter value 10
print(message(20)) # will use the provided argument value 20

#named arguments
def movie_screening(movie_name, time):
    print("The movie", movie_name, "will be screened at", time)

movie_screening(movie_name="100 Meters", time="7:00 PM")

def calculate_bmi(weight,height):
    bmi = weight / (height ** 2)
    return bmi

print(calculate_bmi(70, 1.75))

def add_and_subtract(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    return sum_result, difference_result

sum_result, difference_result = add_and_subtract(2,2)
print("Sum", sum_result)
print("Difference", difference_result)


#nested functions 
def anime(name):
    def browse(genre):
        return name +" :"+ genre
    watch = browse("fantasy")
    return watch

print(anime("Witch Hat Atelier"))

#lambda functions
