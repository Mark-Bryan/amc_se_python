students = {
    "Akika" : "Male",
    "Fotsing" : "Male",
    "Blessing" : "Male",
    "Ryan" : "Male"
}

print(f"Fotsing is a {students['Fotsing']}")

print("Is Ryan a student?", "Ryan" in students)

students["Patrick"] = "Male"

print(students)

print(students.keys())

for student in students:
    print(f"{student} is a {students[student]}")

    student_grades = {
    "Ryan": {
        "Chemistry": "A",
        "Physics": "A",
        "Maths": "A",
        "Biology": "A",
        "Biology": "A",
    },
    "Blessing":{
        "Geography": "A",
        "Maths": "A",
        "Economics": "A",
        "ICT": "A",

    },
    

    }

    print("Ryan's Biology Mark: ", student_grades["Ryan"]["Biology"])

    print("Blessing's Economics Grade: ", student_grades["Blessing"]["Economics"])
    

    