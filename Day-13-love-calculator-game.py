# LIVE DEMO: https://replit.com/@guardianblossom/Day-13-love-calculator#main.py
logo = """  _                       _____      _            _       _             
 | |                     / ____|    | |          | |     | |            
 | |     _____   _____  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |    / _ \ \ / / _ \ | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| (_) \ V /  __/ | |___| (_| | | (__| |_| | | (_| | || (_) | |   
 |______\___/ \_/ \___|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                        
                                                                        """
print(logo)

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")  # What is your name?
name2 = input("What is their name? ")  # What is their name?

s = (name1 + name2).lower()
t = s.count("t")
r = s.count("r")
u = s.count("u")
e = s.count("e")
true = t + r + u + e
l = s.count("l")
o = s.count("o")
v = s.count("v")
e = s.count("e")
love = l + o + v + e
score = int(str(true) + str(love))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
