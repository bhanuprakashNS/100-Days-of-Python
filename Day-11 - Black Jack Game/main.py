#....................... Blackjack Project................................ #
# .... Created and Modified by N.S.Bhanuprakash on 15-03-2022 .............#
# ...........Created in replit ..................... #

import random
from replit import clear 
from art import logo


def sum_cards(cards) :
  if sum(cards) == 21 and len(cards) == 2 :
    return 0
    print("black jack!")
  elif 11 in cards and len(cards) == 2 :
    cards.remove(11)
    cards.append(1)
    return sum(cards)
  else :
    return sum(cards)

def ask_another_card():
 
  card_set = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]

  cards = random.choice(card_set)
  return cards
  
def compare(currentscore,dealerscore):
  if currentscore > 21 :
    print("You lose")
  elif currentscore <= 21 and dealerscore <=21:
    if dealerscore < currentscore :
      print("You win")
    elif dealerscore > currentscore :
      print("You lose")
    elif dealerscore == currentscore :
      print("Draw")
  elif currentscore>21 and dealerscore > 21 :
    print("You lose")
  elif dealerscore > 21 :
    print("You win")
    
def another_game():
  # clear()
  print(logo)
  anothergame = input("Do you want to play black jack? Type 'y' or 'n'\n")
  if anothergame == 'y' :
    clear()

    user_cards = []
    dealer_cards = []
    current_score = 0

    for _ in range(2):
      user_cards.append(ask_another_card())
      dealer_cards.append(ask_another_card())

    current_score = sum_cards(user_cards)
    dealer_score = dealer_cards[0]

    print(f"User cards set is {user_cards}")
    print(f"User's current score is {current_score}")
    
    print(f"Dealer's first card is {dealer_cards[0]}")
    print(f"dealer's current score is {dealer_score}")

    end_game = False
    
    while end_game is False :
      another_usercard = input("Type 'y' to get another card and type 'n' to pass\n")
  
      if another_usercard == 'y' :
        user_cards.append(ask_another_card())
        current_score  = sum_cards(user_cards)
        dealer_score = sum_cards(dealer_cards)
        print(f"User's card set is {user_cards} and the current score is {current_score}")

        if current_score > 21 :
          print("You lose")
          another_game()
        else :
          end_game = False
        
      elif another_usercard == 'n' :
        while dealer_score < 17 and dealer_score != 0 :
          dealer_cards.append(ask_another_card())
          dealer_score = sum_cards(dealer_cards)
        print(f"User's final card set is {user_cards} and the current score is {current_score}")
        print(f"dealer's final card set is {dealer_cards} and score is {dealer_score}")
        compare(current_score, dealer_score)
        end_game = True

    another_game()
another_game()
