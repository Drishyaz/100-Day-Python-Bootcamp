#If the bill was $150.00, split between 5 people, with 12% tip. 

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_tips = (bill / people) * (tip / 100 + 1.0)
# ONE WAY
#total_tips = round(total_tips,2)  # 33.6
# ANOTHER WAY
total_tips = "{:.2f}".format(total_tips)
print(f"Each person could pay: ${total_tips}")

# LIVE DEMO: https://replit.com/@guardianblossom/tip-calculator-start#main.py
