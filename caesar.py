import sys
### Dropdown Menu ###
print("""
Hi there! Please choose one of the options
1. Encrypt
2. Decrypt
""")
option = input('Option: ')

### Functions ###
def check(text): # This function takes in the plaintext and checks whether or not there are any digits or special characters
    plaintextArray = text.split() # Splitting the plaintext into a list of strings
    for words in plaintextArray: # Checking the strings for any numbers or special characters
        if words.isalpha() == False:
            sys.exit("There Should Not Be Any Numbers Or Special Characters In Your Plaintext / Ciphertext")
    return text

def encrypt(plaintext,key): # This function takes in the plaintext as well as an integer value as the key and encrypts it
    ciphertext = ''
    for i in range(len(plaintext)): # Splitting the plaintext into strings
          char = plaintext[i]
          char = char.lower() # Setting the strings to lowercase
          charUnicode = ord(char) # Getting the unicode value for the strings
          encryption = charUnicode + key # Encrypting
          space = ord(' ') + key
          if encryption == space: # Checking whether there is space bar or not
              encryption = ord(' ')
          else:
              while encryption > ord('z'): # New iteration
                  encryption -= 26
          convert = chr(encryption) # Converting back the unicode characters to ASCII characters
          ciphertext += convert # Putting all the broken up strings back into one line of string
    return ciphertext

def decrypt(ciphertext, key): # This function takes in the ciphertext as well as an integer value as the key and decrypts it
    plaintext = ''
    for i in range(len(ciphertext)): # Splitting the ciphertext into strings
        char = ciphertext[i]
        char = char.lower() # Setting all the strings to lowercase
        charUnicode = ord(char) # Getting the unicode value for the strings
        decryption = charUnicode - key # Decrypting
        space = ord(' ') - key
        if decryption == space: # Checking whether there is space bar or not
            decryption = ord(' ')
        else:
            while decryption < ord('a'): # New iteration
                decryption += 26
        convert = chr(decryption) # Converting back the unicode characters to ASCII characters
        plaintext += convert # Putting all the broken up strings back into one line of string
    return plaintext

### Conditions ###
if option == '1':
    plaintext = input('Please Enter Your Plaintext: ')
    key = input('Please Enter Your Key: ')
    if key.isdigit() == False:
        sys.exit('Please Enter A Valid Key With Only Numbers')
    else:
        key = int(key)
        plaintext = check(plaintext)
        ciphertext = encrypt(plaintext,key)
        print(ciphertext)

elif option == '2':
    ciphertext = input('Please Enter Your Ciphertext: ')
    key = input('Please Enter Your Key: ')
    if key.isdigit() == False:
        sys.exit('Please Enter A Valid Key With Only Numbers')
    else:
        key = int(key)
        ciphertext = check(ciphertext)
        plaintext = decrypt(ciphertext,key)
        print(plaintext)

else:
    sys.exit('Please Enter A Valid Option')
