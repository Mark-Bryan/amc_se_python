userProfile = {
    "firstName": "Banyeh",
     "lastName" : "Akika",
     "favouriteColor" : "blue",
 }
print(userProfile)

user_data = {}
user_db = open("user_profile.txt", 'r')

for userProp in user_db:
    keyValuePair = userProp.split(":")
user_data[keyValuePair[0]] = keyValuePair[1].strip("\n")

user_db.close()

print("Dynamic User Data", user_data)


required_fields = {
     "firstName":"First Name",
     "lastName": "Last Name",
     "emailAddress": "Email Address",
    "password": "Password"

 }

user_info = {}
for field in required_fields.keys():
    user_info[field] = input(f"Enter your {required_fields[field]}: ")

print(user_info)

user_file = open(f"{user_info['emailAddress']}.txt", 'w')

for prop in user_info.keys():
     user_file.write(f"{prop}:{user_info[prop]}\n")
user_file.close()


#  Amend the program to start by asking the user what action they would like to complete. 

#  Option 1: Save information to user file
# Option 2 : Retrieve information from a user file

#  If the user chooses option 1, execute the block of code we have just created in part 1
#  If the user chooses option 2, ask for their email address and retrieve their information from their file


def save_your_info():
    user_info = {}
    for field in required_fields.keys():
        user_info[field] = input(f"Enter your {required_fields[field]}: ")

def retrieve_user_info():
    print("Option 2")
    userEmail = input("Please enter your email address to retrieve your info")
    fileName = (f"{userEmail}.txt")

while True:
    print("\nSelect an action:")
    print("1: Save information to user ")
    print("2: Retrieve information from a user ")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        save_your_info()
    elif choice == '2':
        retrieve_user_info()
    break
    
    





