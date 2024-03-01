# LIVE DEMO: https://replit.com/@guardianblossom/guess-the-number-start#main.py

logo = '''    _   __                   __                   ______                          _              
   / | / /__  __ ____ ___   / /_   ___   _____   / ____/__  __ ___   _____ _____ (_)____   ____ _
  /  |/ // / / // __ `__ \ / __ \ / _ \ / ___/  / / __ / / / // _ \ / ___// ___// // __ \ / __ `/
 / /|  // /_/ // / / / / // /_/ //  __// /     / /_/ // /_/ //  __/(__  )(__  )/ // / / // /_/ / 
/_/ |_/ \__,_//_/ /_/ /_//_.___/ \___//_/      \____/ \__,_/ \___//____//____//_//_/ /_/ \__, /  
                                                                                        /____/   '''

print(logo)

#Number Guessing Game

import random

def game(attempts):
  # this will store the original no. of attempts
  total_chances = attempts + 1
  # the computer randomly chooses a number between 1 to 100
  number = random.randint(1,100)

  # the below loop runs until no more attemtps left.
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

# the following if blocks, hint you about what the number is.
    if guess < number:
      print("Too low.")
    elif guess > number:
      print("Two high.")
    else:
      print(f"You got it! The answer was {number}.\nYou guessed it in {total_chances - attempts} guesses.")
      return

    # if it isn't your last attempt, then you won't have to guess again.
    if attempts - 1 != 0:
      print("Guess again.")
    # every time you lose an attempt if you make a wrong guess
    attempts -= 1

  print("You have run out of guesses, you lose..")  


print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

guesses = 0
# this is a global variable since defined outside of function.
if difficulty == 'easy':
  guesses = 10
  game(guesses)
elif difficulty == 'hard':
  guesses = 5
  game(guesses)
else:
  print("Input Error. Please type 'easy' or 'hard'.")
