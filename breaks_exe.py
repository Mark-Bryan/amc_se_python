"""
Write a program that asks the user for 5 numbers
If the user enters a number greater than 100, skip that number and continue with the next(use continue)
After all inputs, print the valid numbers entered

"""
"""
Create a program that prints numbers from 1 to 30, but stops completely when it encounters a multiple of7 7( use break)

"""
number = []
for num in range(5):
    num = int(input('Please input a number: '))
    if num > 100:
        continue
    number.append(num)

print(number)







 
for num in range(1, 30):
    if num % 7 == 0:
        break

    print(num)


