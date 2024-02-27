# LIVE DEMO: https://replit.com/@guardianblossom/blind-auction-start#main.py
from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
#HINT: You can call clear() to clear the output in the console.
print(logo)
bids = {}
bidding_finished = False

# bidding_record = {"Diya" : 123, "Drish" : 321}
def find_highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      
  print(f"The highest bid amount is ${highest_bid} by {bidder}")
  
while not bidding_finished:
    bidder_name = input("What is your name? ")
    bid_amount = int(input("What is your bid amount ? $"))
    bids[bidder_name] = bid_amount
    should_continue = input("Are there other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "no":
      find_highest_bidder(bids)
      bidding_finished = True
    elif should_continue == "yes":
      bidding_finished = False
      clear()
