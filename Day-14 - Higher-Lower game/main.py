#....................... 'Higher-Lower game' ................................ #
# .... Created and Modified by N.S.Bhanuprakash on 18-03-2022 .............#
# ...........Created in replit ..................... #
import random
from art import logo, vs
from game_data import data
from replit import clear

print(logo)
A = random.choice(data)
game_over = False
score = 0

def get_data(dataset):
  """Gets the values in the dataset for their corresponding keys"""
  name = dataset["name"]
  description = dataset["description"]
  country = dataset["country"]
  return f"{name}, {description}, {country}"

def compare(user_response , compared_against) :
  """Compares the user response dataset followers with the opposite dataset followers and gives the result"""
  global score, game_over
  clear()
  print(logo)
  if user_response["follower_count"] > compared_against["follower_count"] :
    score += 1
    print(f"You are correct and your current score is {score}")
  elif user_response["follower_count"] < compared_against["follower_count"] :
    game_over = True
    print(f"You are wrong and your final score is {score}")

while game_over is False :
  B = random.choice(data)
  if A == B :
    B = random.choice(data)
  print (f"compare A: {get_data(A)}")
  print (vs)
  print (f"against B: {get_data(B)}" )
  response = input("who has more followers A or B?\n").upper()
  if response == "A" :
    user_response = A
    compared_against = B
  elif response == "B" :
    user_response = B
    compared_against = A
  compare(user_response, compared_against)
  A = user_response
