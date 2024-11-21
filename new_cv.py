cv_builder = {
    "Name": {
        "first_name": "Bruce",
        "last_name": "Wayne",
    },
    "occupation": "CEO of Wayne Enterprise",
    "About Me": "My name is Bruce Wayne and I am also known as the Dark Knight of Gotham City",
    "Synopsis": "Hi there ! My name is Bruce Wayne, I am a Banker",
    "qualifications": [
        {"name": "Ordinary Level", "description": "11 papers"},
        {"name": "Advanced Level", "description": "5 papers"},
        {
            "name": "Degree in Micro Economics",
            "description": "Best graduating student in New Brunswick Community College",
        },
    ],
}
print(cv_builder)


"""
CV for first_name last_name
occupation

About Me
Synopsis

Qualifications
----
qualification_name
qualification_description
---
"""


print(" First Name: ", cv_builder["Name"]["first_name"])
print(" Last Name:", cv_builder["Name"]["last_name"])

print(" Occupation:", cv_builder["occupation"])

print("About Me:", cv_builder["Synopsis"])


print("Qualifications:", cv_builder["qualifications"][0]["name"])
print(" Qualifications:", cv_builder["qualifications"][0]["description"])

print(" Qualifications: ", cv_builder["qualifications"][1]["name"])
print(" Qualifications:", cv_builder["qualifications"][1]["description"])


"""

Enhance the CV builder program to accept the required information from a user

Ask the user for their;

 -First Name
 -Last Name
 -Occupation
 -Synopsis(A brief description)
 -Qualifications*

 *You could ask the user how many qualifications they want to add and beased on their response request the information you need. 

 Use the information received to populate a CV Builder object and when they are ready, print their CV to the screen

"""

firstName = input("Input your First Name: ")
lastName = input("Enter your last Name: ")

print("First name : ", firstName["Name"]["first_name"])
print("Last name : ", lastName["Name"]["last_name"])

cv_builder["Name"]["first_name"] = firstName
cv_builder["Name"]["last_name"] = lastName

Occupation = input("Enter your present occupation")
print(Occupation)
cv_builder["occupation"] = Occupation

AboutMe = input("Enter information about yourself")
print(AboutMe)
cv_builder["About Me"] = AboutMe

Synopsis = input("Give a brief decription of your synopsis")
print(Synopsis)
cv_builder["Synopsis"] = Synopsis

qualifications = input("Enter your qualifications")
print(qualifications)
cv_builder["qualifications"] = qualifications

print(cv_builder)
