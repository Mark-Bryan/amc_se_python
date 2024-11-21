# Create a simple dictionary
akika = {"name": "Banyeh", "date_of_birth": "14 Sept 2005", "favourite_team": "Chelsea"}

# Access the date_of_birth key and print the value
print("Birthday :", akika["date_of_birth"])

print("Favourite Team :", akika["favourite_team"])

favourite_teams = {"Premier League": "Chelsea", "La Liga": "Real Madrid"}

# Replacing the value of name

akika["name"] = "Akika"
print("name:", akika["name"])

akika["favourite_team"] = favourite_teams
print("favourite team", akika["favourite_team"])

print("Favourite team in La Liga:", akika["favourite_team"]["La Liga"])
print("Favourite team in Premier League:", akika["favourite_team"]["Premier League"])

akika["favourite_team"]["Serie A"] = "Inter Milan"
print("favourite team:", akika["favourite_team"]["Serie A"])

############################
############################
############################

student_results = {
    "Jessica": {
        "Chemistry": "A",
        "Biology": "B",
        "Mathematics": {
            "Pure": "A",
            "Mechanics": "B+",
        },
        "Physics": "A",
        "Further Mathematics": "C",
    },
    "Thomas": {
        "Latin": "C",
        "History": "A",
        "Economics": "B+",
        "Literature": "A-",
        "Art": "C",
    },
}

# What did Jessica score in Chemistry?

print("Jessica's Chemistry Score:", student_results["Jessica"]["Chemistry"])

# What did Thomas score in Economics?

print("Thomas' Economics Score: ", student_results["Thomas"]["Economics"])

# What did Jessica score in Pure Mathematics?

print("Jessica's Pure Mathematics Score:", student_results["Jessica"]["Mathematics"]["Pure"])

# There was a mistake in Thomas' Art grade. It should be a B. Correct the grade.

student_results["Thomas"]["Art"] = "B"
print("Thomas' Art grade:", student_results["Thomas"]["Art"])



