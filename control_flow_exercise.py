"""
1. Write a program that prints all the even numbers between 1 and 50
2. Check if a number is prime(input from the user). If it is prime, print "Prime"; otherwise, print "Not Prime"
3. Write a program that prints the sum of all numbers from 1 to 100 that are divisible by 3
4. Create a program that asks for 5 numbers from the user, then prints the largest number
5. Write a program that counts how many vowels are in a given string(input from user)
6. Create a program that prints the Fibonacci sequence up to the 10th term
7. Write a program that reverses the digits of a integer


"""
# 1. Write a program that prints all the even numbers between 1 and 50

for num in range(1, 50):
    if num % 2 == 0:
        print(num)


#2. Check if a number is prime(input from the user). If it is prime, print "Prime"; otherwise, print "Not Prime"
number = int(input('Any Number : '))

is_prime = True
for run in range(2, number):
    if(number)% run == 0:
        is_prime = False
        break

if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


#3. Write a program that prints the sum of all numbers from 1 to 100 that are divisible by 3
total = 0
for num in range(1, 101):
    if num % 3 == 0:
        total += num #total=total+num
print (total)


#4. Create a program that asks for 5 numbers from the user, then prints the largest number

numbers = []
 
for i in range(5):
    numbers = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

highest_number = max(numbers)    
print(f"The highest number is {highest_number}")


# 5.Write a program that counts how many vowels are in a given string(input from user)
sentence = input("Enter a string to find out how many vowels it contains: ")

vowels = ('a', 'e', 'i', 'o', 'u')
vowel_count = 0

for letter in sentence.lower():
    if letter in vowels:
        vowel_count += 1

print(f"There are {vowel_count} vowels in the sentence '{sentence}")


#6. Write a program that prints the Fibonacci sequence up to the 10th term
x = y = 1
while y < 100:
    print(y)
    x, y = y, x + y



#7. Write a program that reverses the digits of a integer

random_number = input("Enter any number: ")#2345

current_character = len(random_number) - 1
reversed_number = ''
while(current_character >= 0):
    reversed_number += random_number[current_character]#reversednum=reversednum + random num
    current_character -= 1

print(f"{random_number} reversed is {reversed_number}")

#8. Check if a word (input from the user) is a palindrome
palindrome = input('Enter a word that reads forward and backward')
len_palindrome = len(palindrome) - 1
reversed_palindrome = ''
while(len_palindrome > 0):
    reversed_palindrome += palindrome[len_palindrome]
    len_palindrome-=1
print(reversed_palindrome)

if palindrome == reversed_palindrome:
    print(f"{palindrome} is a palindrome")
else:
    print(f"{palindrome} is not a palindrome")

#9. Write a program that calculates the factorial of a number(input from the user)

factorial = int(input('Please enter a number'))
i = 1
j = 1
while i <= factorial:
    j *= i
    i += 1
print(j)

#10. Create a program that prints all the numbers from 1 to 100, but for multiples of 3 print "Fizz", for multiples of 5 print "Buzz", and for multiples of both 3 and 5 print "FizzBuzz"


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')

    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

