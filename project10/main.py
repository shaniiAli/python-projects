def encrypt(message, key):
    result = ""
    
    for char in message:
        if char.isalpha(): 
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += char  
            
    return result


def decrypt(message, key):
    return encrypt(message, -key)


print("Caesar Cipher")

while True:
    choice = input("Choose (e)ncrypt or (d)ecrypt: ").strip().lower()

    if choice == 'e':
        message = input("Enter your message: ")
        try:
            key = int(input("Enter the key (shift value) between 1 and 26: "))
            
            if not (1 <= key <= 26):
                raise ValueError
            
            print("Encrypted Message:", encrypt(message, key))
        
        except ValueError:
            print("Invalid key. Please enter an integer between 1 and 26.")


    elif choice == 'd':
        message = input("Enter your message: ")
        try:
            key = int(input("Enter the key (shift value) between 1 and 26: "))
            
            if not (1 <= key <= 26):
                raise ValueError
            
            print("Decrypted Message:", decrypt(message, key))
        
        except ValueError:
            print("Invalid key. Please enter an integer between 1 and 26.")


    else:
        print("Invalid choice. Please choose 'e' or 'd'.")
