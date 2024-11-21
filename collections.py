# A set holds unique values. It is mutable
#This means it can be changed after creation
mySubjects = set()

# A set cannot be changed once it has been created
#it is non mutable
mandatory_subjects = ('English', 'French', 'Maths')

mySubjects.update(mandatory_subjects)

# a list holds ordered objects. It is mutable
elective_subjects = [
    "Geography",
    "Economics",
    "Biology",
    "Physics",
    "Additional Maths",
    "ICT",
    "Literature",
    "History",
    "Religious Studies",
]

subjects_offered = int(input("How many subjects would you like to offer"))

subjects_chosen = 0

while subjects_chosen < subjects_offered:

# To change a subjects, enter the corresponding number;
# [1] Geography, [2] Economics,......, [9] Religious Studies

  print("To choose a subject, enter the corresponding number...")

i = 0
while i < len(elective_subjects) - 1:
    print(f'[{i + 1}] {elective_subjects[i]},' ,end='')
    i += 1

print(f'[{i + 1}] {elective_subjects[i]}')

#Ask the user to select the subject they would like to take
choice = input(f"Enter subject number(1-{len(elective_subjects)}): ")

mySubjects.add(elective_subjects[int(choice)-1])

subjects_chosen += 1


print(mySubjects)


# Add the corresponding subject to the mySubjects set correcting for the index offset







