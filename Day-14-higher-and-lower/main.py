# LIVE DEMO: https://replit.com/@guardianblossom/day-14-higher-lower-start#main.py
from art import logo, vs

import random
from game_data import data


def generate_option():
    """Get data from a random account"""
    return random.choice(data)


def format_data(data):
    """Format account data into readable format: name, description and country"""
    return f"{data['name']}, a {data['description']}, from {data['country']}."


def follower_count(account):
    """Returns the followers count of the specified account"""
    return account['follower_count']


def check_answer(user_choice, count_a, count_b):
    """Checks if the choice made by user is the correct choice"""

    # which one has more followers ? A or B ?
    ans = max(count_a, count_b)

    # checks if user's choice and the max followers have the same option
    if (ans == count_a and user_choice == 'A') or (ans == count_b and user_choice == 'B'):
        return True
    else:
        return False


def game():
    """The main function that starts the game.
  It displays 2 options, where the user has to choose which account has more followers.
  Awarded with one point if the guess is correct, otherwise Game Over.."""
    # print(logo)
    # keeps track of user's current score
    score = 0
    should_continue = True
    # randomly get two account's data in choice A and B
    choice_a = generate_option()
    choice_b = generate_option()

    while should_continue:
        # whenever the user decides to continue the game,
        # 2nd option from previous round becomes 1st option in next round
        choice_a = choice_b
        choice_b = generate_option()

        # ofc if both options are same, we need to change the other one
        while choice_a == choice_b:
            choice_b = generate_option()

        # display choices A and B in readable format
        print(f"\nCompare A: {format_data(choice_a)}")
        print(vs)
        print(f"Against B: {format_data(choice_b)}")

        # user makes a choice: 'A' or 'B'
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        # we collect the 'follower_count' data for choice A and B
        followers_a = follower_count(choice_a)
        followers_b = follower_count(choice_b)

        # debugging - what's the follower count for A and B ?
        name_a = choice_a['name']
        name_b = choice_b['name']
        print(f"{name_a}'s count: {followers_a}, {name_b}'s count: {followers_b}")

        # check if user's guess is correct or nah
        is_correct = check_answer(user_choice, followers_a, followers_b)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry that's wrong.. Final score: {score}")
            should_continue = False


game()
