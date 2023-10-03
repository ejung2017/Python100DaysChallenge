alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift_amount): 
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position] 
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}") 

# def decrypt(plain_text, shift_amount): 
#     cipher_text = ""
#     for letter in plain_text: 
#         position = alphabet.index(letter)
#         new_position = position - shift_amount 
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter 
#     print(f"The decoded text is {cipher_text}")

# if direction == "encode": 
#     encrypt(text, shift)
# elif direction == "decode": 
#     decrypt(text, shift)
# else: 
#     print("Type 'encode' to encrypt, type 'decode' to decrypt")

   
#TODO-combine encrypt() and decrypt() into one single function caesar() 

def caesar(directions, texts, shifts): 
    cipher_text = ""
    for letter in texts: 
        position = alphabet.index(letter)
        if directions == "encode": 
            new_position = position + shifts 
        elif directions == "decode": 
            new_position = position - shifts 
        new_letter = alphabet[new_position]
        cipher_text += new_letter 
    print(cipher_text)

caesar(direction, text, shift)