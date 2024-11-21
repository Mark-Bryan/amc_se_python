# if condtion
number = 4
if number == 4:
    print("Number = 4")

if number > 3:
    print("Number is greater than 3")

if number > 3 and number < 5:
    print("Number is 4")

if number %2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

    ##################
    ##################
    ##################

"""
ask the user for a number
if the number is greater than 10 tell the user that it is greater than 10
if the number is less than 10 tell the user it is less than or equal to 10
if the number is a multilple of 3 tell the user it is a multiple of 3
if it is not a multiple of 3 tell the user it is not a multiple of 3

"""

number = int(input('Any Number : '))

if number > 10:
    print("The number is greater than 10")

else:
    print("Your number is less than 10")

if number % 3 == 0:
    print('This number is a multiple of 3')

else:
    print('The number is not a multiple of 3')

    
    #if elif else checks multiple conditions
    
if number % 2 == 0:
    print(f"{number} is an even number")
elif number % 3 == 0:
    print(f"{number} is a multiple of 3")

else:
    print(f"{number} is neither an even number or a multiple of 3")


    
#loops

fruits = ['apples', 'bananas', 'cherries', 'dates']

for fruit in fruits:
    print(fruit)

for number in range(5) :
        print(number)

for number in range(len(fruits)):
    print(f"{number + 1}.{fruits[number]}")

    # default range(number_of_items)
    #starting position: range(number_of_items, starting_position, increment)

    # ask the user for a number and output the timestable of that number from 1 to 12

timestable = int(input("Enter any number : "))

for num  in range(1, 12):
    print(f'{timestable} x {num} = ', timestable*num)



# Display only multiples of 3 from 1 - 30
for num in range(1, 30):
    if num % 3 == 0:
        print(num)
    else:
        continue 
    print("This is not a multiple of 3")

for num in range(1, 31):
    print("The current number is ", num)
    continue
    print("You will not see this code executed")

    # find the first prime number in a range
    

