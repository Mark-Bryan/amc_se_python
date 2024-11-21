import os # This line imports another module and it's use to check whether a given file or directory is present 
def save_name(first_name, last_name):
   user_info =  open("user_info.txt", "w") 
   user_info.write(f"First Name: {first_name}\n")
   user_info.write(f"Last Name: {last_name}\n")
   user_info.close()
print("First and last names have been saved to user_info.txt.")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
save_name(first_name, last_name)


def save_dob(dateOfBirth):
 user_info =  open("user_info.txt", "a") 
 user_info.write(f"Date of Birth: {dateOfBirth}\n")
 user_info.close()

print("Date of Birth has been added to user_info.txt.")


def update_user_info():
  
  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")

  if os.path.exists("user_info.txt"): # This line of code checks whether the file user_info.txt exists
    file = open ("user_info.txt", 'r') 
    present_info = file.read()
    file.close()
    print("Present Information has been found: ")
    print(present_info)

    change_values = input("\nWould you like to change any of your values? : ")
    if change_values == 'yes':
  
      first_name = input("Enter your new first name: ")
      last_name = input("Enter your new last name: ")
      dateOfBirth = input("Enter your new date of birth: ")

      save_name(first_name, last_name)
      save_dob(dateOfBirth)
      print('Information has been changed successfully')
    elif change_values == 'no':
       print("No change has been made")
       
    else :
       print("No previous information found. Create a new file ")
dateOfBirth = input("Enter your Date of Birth: ")

        # Save new information
save_name(first_name, last_name)
save_dob(dateOfBirth)

# Run the function to update or create new information
update_user_info()
