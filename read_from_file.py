my_poem = open("my_poem.text", 'r')

for line in my_poem:
    print(line, end = '')

my_poem.close()    