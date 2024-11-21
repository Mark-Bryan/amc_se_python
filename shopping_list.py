# Create am empty shopping list
shoppingList = []

# Create a flag to control our while loop
flag = True

while flag:
    listItem = input("What would you like to add to the shopping list?(When finished send an empty item)")
    

    if (len(listItem) == 0):
        flag = False
    else:
        #otherwise add the item to the shopping list
        shoppingList.append(listItem)
        print("Here's your shopping list so far: ", shoppingList) 

        #When the list is complete, display the users shopping list
    
print("Here's your shopping list: ", shoppingList)

shoppingQuantities = []

index =  0
while index < len(shoppingList):
    shoppingQuantities.append(input(f"What quantity of {shoppingList[index]} do you want"))
    index += 1

    


    print(shoppingList)
    print(shoppingQuantities)

 



    

