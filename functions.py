# Defining a simple function

"""
To define a function , we use the 'def' keyword, followed by the function name and a colon

def functionName:
    indentented code is executed as part of this function
    indentented code is executed as part of this function

"""

def myFunction():
    print("This is my first function")

    """
    To execute the same block of code by calling the function multiple times
    """

myFunction()

"""
We can execute the same block of code by calling the function multiple times
"""

myFunction()
myFunction()
myFunction()

# Create a function called intro which outputs "Hello, my name is my Name"

def intro():
    print('Hello, my name is Akika')

    # Variables defines outside of any function are called global variables
    # They can be accessed from anywhere in the program

name = input("What's your name?")

def greeting():
    print(f"Hello {name}, it's nice to meet you")

greeting()

# Variables defined inside a function are called local variables
# They only exist inside the function in which they they were defined

yearOfBirth = int(input('What year were you born in? '))

def greeting2():
    age = 2024 - yearOfBirth
    print(f"Hello {name}, you look like you're {age} years old")

greeting2()

# The variable 'age' does not exis outside of the greeting2 function
def whatTimeIsIt():
    print(f"The time is currently: {currentTime}")

    whatTimeIsIt()
    currentTime = "7:15"

   # Using arguments means we don't have to rely on globally defined variables for our functions to work

def greeting3(name):
    print(f"Hello {name}, it's nice to meet you")

greeting3("Suhmayah")
greeting3("Ryan")
greeting3("Blessing")
greeting3("Fotsing")
greeting3("Akika")    

greeting3(input("What's your name ? "))

# Create a function that receives  a name and favourite color as arguments and outputs:
# Hi, my name is {name} and my favourite colour is {colour}

name = input("Enter your name : ")
colour = input("Enter your favourite colour: ")


def receiver():
    print(f"My name is {name} and my favourite colour is {colour}")

receiver()



"""
1. Create a function called calculate_area that takes two arguments, length and width, and prints the area of the rectangle.

2. Write a function called find_max that takes three numbers as arguments and returns the largest of the three

"""

# 1. 
length = int(input("Enter your length : "))
width = int(input("Enter your width: "))
area = length * width
def calculate_area(length, width):
    print(f"Area of rectangle is {area}")
calculate_area(length, width)    

#2. 

def find_max(num1, num2, num3):
    largest_number = max(num1, num2, num3)
    print("The largest number is ", largest_number)

find_max(28, 13, 15)




# Named Parameters




def brief_introduction(name, age, address):
    print(f"Hello, my name is {name}. I am {age} years old and I live in {address}")
brief_introduction('Akika', 35, 'Douala')


# Create a function called friendly_greeting that accepts a name and outputs the string
# "Hello {name}, it's nice to meet you.". Set a defaut value for the name argument as "friend"

def friendly_greeting(name = "Tancho"):
    print(f"Hello {name}, it's nice to meet you")
friendly_greeting()

## Returning values from a function

def is_a_prime_number(number_in_question):
    is_prime = True
    for num in range(2, number_in_question):
        if number_in_question % num == 0:
            is_prime = False
            break

    return is_prime
is_prime = is_a_prime_number(73)
print(is_prime)

if is_prime:
    print("73 is a prime number, that was a lucky guess!")
else:
    print("73 isn't a prime number")

if is_a_prime_number(8):
    print("This function is not working correctly")
else:
    is_a_prime_number(int(input("8 is not a prime number. Try another number")))


def area_calculator(length, width):
    area = length * width/2
    return area 
area1 = area_calculator(12,6)
area2 = area_calculator(17,4)
area3 = area_calculator(16,7)
area4 = area_calculator(7,62)
area5 = area_calculator(34,19)

print('The area of triagle 1 is :', area1)
print('The area of triangle 2 is :', area2)
print('The area of triangle 3 is : ', area3)
print('The area of triangle 4 is: ', area4)
print('The area of triangle 5 is : ',area5)

largest_area = max(area1, area2, area3, area4, area5)
print('\n The largest area is ', largest_area)
    

### v2
triangles = [
    {'length': 12, 'width': 6},
    {'length': 17, 'width': 4},
    {'length': 16, 'width': 7},
    {'length': 7, 'width': 62},
    {'length': 34, 'width': 19},
]

triangle_areas =[]
for triangle in triangles:
    triangle_areas.append(calculate_area(length= triangle['length'], width=triangle['width']))

print('\n The Largest area is', max(triangle_areas))