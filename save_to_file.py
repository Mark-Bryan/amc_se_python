# myFile = open("output/my_first_file.txt", 'w')
# myFile.write("Hello, world!")
# myFile.close()

# # Create a file called user_interface
# # Receive a message from a user and save it to the file

# user_interface = open("user_interface", 'w')
# user_interface.write(input("Enter your favourite car brand:"))
# user_interface.close() 
 
poem  = "Roses are red,\n"
poem += "Violets are blue,\n"
poem += "Sugar is sweet,\n"
poem += "...\n"


my_poem = open("output/my_poem.text", "w")
my_poem.write(poem)
my_poem.close

my_poem = open("output/my_poem.text", 'a')
my_poem.write(input("By :"))
my_poem.close()



edit_my_poem = open("output/my_poem.text", 'r+')

# print("Read(): ", edit_my_poem.read(10))
# print("Read(): ", edit_my_poem.read(10))
# edit_my_poem.seek(0)
# print("Read(): ", edit_my_poem.read(20))
# edit_my_poem.seek(25)
# edit_my_poem.write("Lets add some random text")

# edit_my_poem.close()

# edit_my_poem.seek(51)
# edit_my_poem.write("And so are you.\n")
# edit_my_poem.close()

line_counter = 1
for line in edit_my_poem:
    if (line_counter == 3):
        edit_my_poem.write("And so are you. \n")
        break
    line_counter+=1

edit_my_poem.close()
