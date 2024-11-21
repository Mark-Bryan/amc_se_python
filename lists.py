shoppingList = ["flour", "butter", "sugar", "eggs", "baking powder"]
print("Shopping List: ", shoppingList)

miscellanous = []
print("Empty List: ", miscellanous)

miscellanous.append("Football boots")
print("Item added to the list: ", miscellanous)

print("Items in my shopping list: ", len(shoppingList))

print("The first element in my shopping list is", shoppingList[0])

print("The second element in my shopping list is", shoppingList[1])

print("The third element in my shopping list is", shoppingList[2])

print("The fourth element in the shopping list is", shoppingList[3])

print("The fifth element in my shopping list is", shoppingList[4])

#item(n) of the shopping list is shoppingList[n]

index = 0

while index < len(shoppingList):
    print(f"Item {index + 1} of the shopping list is {shoppingList[index]}")
    index += 1
