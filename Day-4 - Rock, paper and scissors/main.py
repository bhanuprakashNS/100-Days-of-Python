# ...............Rock, Paper and Scissors game ...........#
# Created and Modified by N.S.Bhanuprakash in January 2022 .............#
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]

human = input("what do you want to choose? Rock, paper or scissors?\n").lower()
if human == "rock":
    print(game_images[0])
elif human == "paper":
    print(game_images[1])
elif human == "scissors":
    print(game_images[2])
else:
    print("Choose one among the three!")
    quit()

computer = random.randint(0, 2)
if computer == 0:
    print("Computer chooses rock")
    computer = 'rock'
    print(game_images[0])
    if human == 'rock':
        print("Draw match!")
    elif human == 'paper':
        print("You Won!")
    elif human == 'scissors':
        print("You Lose!")
elif computer == 1:
    print("Computer chooses paper")
    computer = 'paper'
    print(game_images[1])
    if human == 'rock':
        print("You Lose!")
    elif human == 'paper':
        print("Draw match!")
    elif human == 'scissors':
        print("You Won!")
elif computer == 2:
    print("Computer chooses scissors")
    computer = 'scissors'
    print(game_images[2])
    if human == 'rock':
        print("You Won!")
    elif human == 'paper':
        print("You Lose!")
    elif human == 'scissors':
        print("Draw match!")
