#....................... 'Guess The Number' game................................ #
# .... Created and Modified by N.S.Bhanuprakash on 16-03-2022 .............#
# ...........Created in replit ..................... #
import random
from art import logo
print(logo)
print("Welcome to 'Guess The Number' game!")
print("I'm thinking a number between 1 to 100. Can you guess it?")
number_set = []
for number in range(1,101):
  number_set.append(number)
computer_guess = random.choice(number_set)


def guess_number(iteration_number): 
  chances = iteration_number
  while chances > 0 :
    guessed_number = int(input("Guess a number?\n"))
    if guessed_number == computer_guess :
      print("You won!")
      quit()
    elif guessed_number != computer_guess :
      if guessed_number > computer_guess:
        print(f"The guessed number {guessed_number} is too high!")
      elif guessed_number < computer_guess:
        print(f"The guessed number {guessed_number} is too low!")
      print("You have lost a chance!")
    chances -= 1
  print(f"You lost the game! The computer's guess is {computer_guess}")
  
difficulty = input("Choose a difficulty level - Easy or Hard?\n").lower()
if difficulty == 'hard':
  print("you have 5 attempts to guess the number.")
  iteration_number = 5 
  guess_number(iteration_number)
elif difficulty == 'easy':
  print("you have 10 attempts to guess the number.")
  iteration_number = 10
  guess_number(iteration_number)

    