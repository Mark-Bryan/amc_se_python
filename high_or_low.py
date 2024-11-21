import random 

a = 5
b = 9

print(a, b)

if(a > b):
   print(f"{a} is greater than {b}")
else:
   print(f"{a} is less than {b}")

number1, number2 = random.randint(1,9)

print(number1, number2)

print("The first number is: ", number1)
answer = input("Guess if the second numbr is higher or lower?(Enter < or > to answer)")

while answer != '>' and answer !='<':
   
   guess = input("Enter'>' if you think the second number is higher or '<' if you think it is lower:")

   if(answer == "<"):
      if number2 < number1:
         print(f"Correct, {number2} is less than {number1}")
        

        
           















print("The first number is", number1)
answer = input("")