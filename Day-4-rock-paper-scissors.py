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
# 1 - rock, 2 - paper, 3 - scissors
comp_choice = random.randint(1,3)
user_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors. "))
ops = [rock,paper,scissors]
print(f"You chose {ops[user_choice-1]}")
print(f"Computer chose {ops[comp_choice-1]}")

if (user_choice == 1 and comp_choice == 1) or (user_choice == 2 and comp_choice == 2) or (user_choice == 3 and comp_choice == 3):
  print("Tie")
  
elif user_choice == 1 and comp_choice == 2:
  print("Computer wins")
elif user_choice == 2 and comp_choice == 1:
  print("You win")
  
elif user_choice == 1 and comp_choice == 3:
  print("You win")
elif user_choice == 3 and comp_choice == 1:
  print("Computer wins")

elif user_choice == 2 and comp_choice == 3:
  print("Computer wins")
elif user_choice == 3 and comp_choice == 2:
  print("You win")

#LIVE DEMO: https://replit.com/@guardianblossom/rock-paper-scissors-start#main.py
