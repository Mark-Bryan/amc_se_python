#calculate the ingredients required for 1 person
flour_pp = 225/4
butter_pp = 225/4
sugar_pp = 150/4
eggs_pp = 4/4
baking_powder = 2/4
#Write a progarm to calculate the ingredients required for the number of people indicated by the user

numberOfPeople = int(input("How many people will you be baking for?"))
total_flour = numberOfPeople * flour_pp
total_butter = numberOfPeople * butter_pp
total_sugar = numberOfPeople * sugar_pp
total_eggs = numberOfPeople * eggs_pp
total_baking_powder = numberOfPeople * baking_powder

#Output the recipe for that many people

print (f"To bake a cake for{numberOfPeople} people you will need:")
print (f"{total_flour}g of flour")
print (f"{total_butter}g of butter")
print (f"{total_sugar}g of sugar")
print (f"{total_eggs} eggs")
print (f"{total_baking_powder}tsp of baking powder")
