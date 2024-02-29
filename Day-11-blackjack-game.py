# LIVE DEMO: https://replit.com/@guardianblossom/day-11-blackjack-start
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
print(logo)
import random

#######################################################
def draw_card(my_turn):
  print(deck)
  random.shuffle(deck)
  card = deck.pop()
  if my_turn:
    my_cards.append(card)
  elif not my_turn :
    computer_cards.append(card)

#######################################################
def find_winner(my_total,dealer_total):
  '''This functions compares the total of the two lists and finds the player with the max score'''
  # debugging - my and dealer's total
  print(f"Computer score: {dealer_total}, Your score: {my_total}")
  if my_total == dealer_total:
    print("Draw!")
    return
    
  if my_total == 21:
    print("You Win!")
  elif dealer_total == 21:
    print("Computer Wins!")
  else:
    if my_total > 21:
      if 11 in my_cards:
        # if ACE counts as 1, is it still over 21?
        my_total -= 1
        if my_total > 21:
          print("You Lose!")
      else:
        print("You Lose!")
    elif my_total > dealer_total:
      print("You Win!")
    else:
      print("You Lose!")
      
#######################################################
def deal_cards ():
  '''This function deals 2 cards each to the player and the computer'''
  for x in range(4):
# computer draws random 2 cards from the deck
    if x >= 2:
      card = random.choice(deck)
      computer_cards.append(card)
    else:
# player draws random 2 cards from the deck
      card = random.choice(deck)
      my_cards.append(card)  
# remove a card from the deck after it has been drawn
    deck.remove(card) 
  
  print(f"Your cards: {my_cards}")
  print(f"Computer's first card: {computer_cards[0]}")
  # debugging - remaining cards on the deck
  print(f"The remaining cards in the deck: {deck}")

#######################################################
# CODE STARTS HERE
# we create a deck of 13 cards
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# we define the two lists beforehand, to modify it whenever
# this way no need to pass and return the lists all the time
my_cards = []
computer_cards = []
deal_cards()
my_total, dealer_total = 0,0

should_continue = True
while should_continue:
  
  my_total = sum(my_cards)
  dealer_total = sum(computer_cards)
  if my_total > 21:
    print("You Lose!")
    break
  
  choice = input("Type 'y' to get another card, 'n' to pass: ").lower()

  # choice is to pass, so the game ends then and there
  if choice == "n":
    print(f"Deck: {deck}")
    
    if dealer_total < 17:
      while dealer_total < 17:
        draw_card(False)
        dealer_total = sum(computer_cards)
        
    (f"Your final hand: {my_cards}")
    print(f"Computer's final hand: {computer_cards}")
    find_winner(my_total,dealer_total)
    should_continue = False

    #new_game = input("Do you want to start a new game? Type y for yes, n for no: ")
    
  # choice is to get another card
  elif choice == "y":
    draw_card(True)
    print(f"Your hand: {my_cards}")
