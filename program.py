# Caesar Cipher Encoding and Decoding

def caesar_encoding(message, shift):
    encoded_message=""
    for char in message:
        if char.isalpha():
            start=ord('a') if char.islower() else ord('A')
            shifted_pos=(ord(char)-start+shift)%26
            encoded_message+=chr(start+shifted_pos)
        else:
            encoded_message+=char
    return encoded_message

def caesar_decoding(encoded_message, shift):
    decoded_message=""
    for char in encoded_message:
        if char.isalpha():
            start=ord('a') if char.islower() else ord('A')
            shifted_pos=(ord(char)-start-shift)%26
            decoded_message+=chr(start+shifted_pos)
        else:
            decoded_message+=char
    return decoded_message
    
while True:
    print("Caesar Cipher Menu:\n1. Encode a message:\n2. Decode a message:\n3. Exit")
    choice=int(input("Enter your choice (1, 2 or 3): "))
    
    if choice==1:
        message=input("Enter a message to encode: ")
        try:
            shift=int(input("Enter the shift value + or - (1 to 25): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 25.")
            exit()
        print("Encoded message:", caesar_encoding(message, shift))
    elif choice==2:
        encoded_message=input("Enter a message to decode: ")
        try:
            shift=int(input("Enter the shift value + or - (1 to 25): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 25.")
            exit()
        print("Decoded message:", caesar_decoding(encoded_message, shift))
    elif choice==3:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select 1, 2 or 3.")
