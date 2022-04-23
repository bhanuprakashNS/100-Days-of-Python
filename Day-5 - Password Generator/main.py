# ..........Password Generator Project ...............#
# Created and Modified by N.S.Bhanuprakash in January 2022......... #

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# letters = random.randint(1,nr_letters)
pw_letters = random.sample(letters, nr_letters)
# print(pw_letters)
pw_numbers = random.sample(numbers, nr_numbers)
# print(pw_numbers)
pw_symbols = random.sample(symbols, nr_symbols)
# print(pw_symbols)

password_letters = []
for i in range(0,len(pw_letters)) :
  password_letters.append(pw_letters[i])
for i in range(0,len(pw_numbers)) :
  password_letters.append(pw_numbers[i])
for i in range(0,len(pw_symbols)) :
  password_letters.append(pw_symbols[i])

# print(password_letters)
random.shuffle(password_letters)
# print(password_letters)
password = str('')
for j in password_letters:
  password+=j
  # password+=random.choice(password_letters)
print(f'your hard password is {password}')
# pw_letter = None
pw_letter = str('')
pw_number = str('')
pw_symbol = str('')

for letter in pw_letters :
  pw_letter += letter
# print(pw_letter)
for number in pw_numbers :
  pw_number += number
# print(pw_number)
for symbol in pw_symbols :
  pw_symbol += symbol
# print(pw_symbol)

print("Your easy password is "+pw_letter+pw_number+pw_symbol)
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P