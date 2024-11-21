#Program to calculate age of an individual

currentYear = 2024
yearOfBirth = input("What year were you born in?")




age = int(currentYear) - int(yearOfBirth)

print(f"By the end of 2024, you will be {age} old.")

if(yearOfBirth.isdigit() == False):
    yearOfBirh = input("what year were you born in? Please provide the value as a number")
    age = currentYear - int(yearOfBirth)

    print(f"By the end of 2024, you will be {age} years old")
    
    if (int (yearOfBirth > currentYear)):
        yearOfBirth = input("You cannot be born in the future. Please enter a year in or before 2024")
        
        age = currentYear - int(yearOfBirth)

        print(f"by the end of 2024 you will be {age} ears old ")
    
