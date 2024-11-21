'''
   The dictionary below contains information about a few prominent artists.

   Interrogate the dictionary to provide the following information:

   1. What is Burna Boy's real name?
   2. How many Instagram followers does Tiwa Savage have?
   3. Which albums has Wizkid released?
   4. Update Rema's YouTube followers to 2 million.
   5. What is the description of Burna Boy's "Twice as Tall" album?
   6. Add a new album for Tiwa Savage called "Water & Garri" with the description "A blend of Afrobeats and soulful R&B, released in 2021."
   7. Extract and print the birthdates of all the artists in the dictionary.
'''

celebrities = {
    "Burna Boy": {
        "real_name": "Damini Ebunoluwa Ogulu",
        "date_of_birth": "1991-07-02",
        "followers": {
            "Instagram": 15000000,
            "Twitter": 7000000,
            "YouTube": 3500000
        },
        "albums": {
            "African Giant": "Released in 2019, this album blends Afrobeat with reggae, dancehall, and pop influences.",
            "Twice as Tall": "Released in 2020, this Grammy-winning album showcases Burna Boy's global Afrobeats sound."
        }
    },
    "Wizkid": {
        "real_name": "Ayodeji Ibrahim Balogun",
        "date_of_birth": "1990-07-16",
        "followers": {
            "Instagram": 16000000,
            "Twitter": 9000000,
            "YouTube": 2500000
        },
        "albums": {
            "Made in Lagos": "Released in 2020, this album highlights a laid-back, international Afrobeats sound.",
            "Ayo": "Released in 2014, this album solidified Wizkid's status as a global Afrobeats star."
        }
    },
    "Tiwa Savage": {
        "real_name": "Tiwatope Savage",
        "date_of_birth": "1980-02-05",
        "followers": {
            "Instagram": 13000000,
            "Twitter": 6000000,
            "YouTube": 2000000
        },
        "albums": {
            "Celia": "Released in 2020, this album celebrates women's empowerment and personal growth.",
            "Once Upon a Time": "Released in 2013, Tiwa's debut album featuring a fusion of Afropop and R&B."
        }
    },
    "Rema": {
        "real_name": "Divine Ikubor",
        "date_of_birth": "2000-05-01",
        "followers": {
            "Instagram": 10000000,
            "Twitter": 3000000,
            "YouTube": 1500000
        },
        "albums": {
            "Rave & Roses": "Released in 2022, this album blends Afrobeats with trap and global pop influences."
        }
    }
}

# Burna Boy's real name and birth date
print("Burna Boy's real name : ", celebrities["Burna Boy"]['real_name'])


# Number of followers Tiwa Savage has and her birth date
print("Number of followers for Tiwa Savage : ", celebrities["Tiwa Savage"]['followers']['Instagram'])


# Number of albums Wizkid has produced and his birth date
print('Number of Wizkid Albums : ', end = '')
for album in celebrities["Wizkid"]['albums'].keys():
    print(f"")


# Updating Rema's Youtube followers 
celebrities["Rema"]['followers']['Youtube'] = 2000000
print("Rema's Youtube Followers: ", celebrities["Rema"]['followers']['Youtube'])

# Describing Burna boys's twice as tall album
print("Decription of Twice As Tall Album : ", celebrities["Burna Boy"]['albums']['Twice as Tall'])

# Adding a new album to Tiwa's savage album collection and giving its description
tiwa_albums = { "Celia": "Released in 2020, this album celebrates women's empowerment and personal growth.",
            "Once Upon a Time": "Released in 2013, Tiwa's debut album featuring a fusion of Afropop and R&B.",
            "Water & Garri " : "A blend of Afrobeats and soulful R & B, released in 2021."
            }
celebrities["Tiwa Savage"]['albums'] = tiwa_albums
print("Updated Album List : ", celebrities["Tiwa Savage"]['albums']) 

for celebrity in celebrities:
    print(f"{celebrity} birthday is{celebrities['celebrity']['date_of_birth']}")

print(celebrities)