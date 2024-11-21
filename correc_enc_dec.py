encryption_key = {
'1' : 'A',
'2' : 'B',
'3' : 'C',
'4' : 'D',
'5' : 'E',
'6' : 'F',
'7' : 'G',
'8' : 'H',
'9' : 'I',
'0' : 'J',
 " ": "Z"
}

decryption_key = {
   'A' : '1',
   'B' : '2',
   'C' : '3',
   'D' : '4',
   'E' : '5',
   'F' : '6',
   'G' : '7',
   'H' : '8',
   'I' : '9',
   'J' : '0',
   'Z' : ' '

}

# Creating reverse code 
def encrypt_string(string):
    encrypted_string = ""

    for letter in string:
        if letter in encryption_key[letter]:
            encrypt_string += letter
        else:
            encrypted_string += letter

    return encrypted_string

def decrypt_string(encrypted_string):
    decrypted_string = ""

    decryption_keys = list(encryption_key.keys())
    for letter in encrypted_string:
        decrypted_letter = decryption_keys[list(encryption_key.values()).index(letter)]
        decrypted_string += decrypted_letter

    return decrypted_string

action = ""
while action == "":
    action = input("Select 1 to Encrypt or 2 to Decrypt: ")

if action == "1":
    plain_string = input("Enter the text to encrypt: ")
    print(encrypt_string(plain_string))

elif action == "2":
    encryption_key = input("Enter the string you want to decrypt: ")
    print(decrypt_string(encrypt_string))

else:
    print("This action is invalid. Please run the program again and select a valid option")

