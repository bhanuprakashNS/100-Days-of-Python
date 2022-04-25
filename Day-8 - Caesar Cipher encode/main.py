# .....................Caesar Cipher (Encode and Decode)...................... #
# ...............Created and modified by N.S.Bhanuprakash on 11-03-2022 ............. #
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    elif char not in alphabet:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")
should_restart = True
while should_restart is True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift%26  
  caesar(start_text=text, shift_amount=shift, 
        cipher_direction=direction)
  restart = input("Do you want to re-start the program - yes or no?").lower()
  if restart == "no":
    should_restart = False
    print("good bye")