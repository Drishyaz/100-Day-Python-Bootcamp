# LIVE DEMO: https://replit.com/@guardianblossom/Day-15-coffee-machine#main.py
MENU = {
  "espresso": {
      "ingredients": {
          "water": 50,
          "milk": 0,
          "coffee": 18
      },
      "cost": 1.50,
  },
  "latte": {
      "ingredients": {
          "water": 200,
          "milk": 150,
          "coffee": 24
      },
      "cost": 2.50,
  },
  "cappuccino": {
      "ingredients": {
          "water": 250,
          "milk": 100,
          "coffee": 24
      },
      "cost": 3.00
  }
}

profit = 0
# original contents of the coffee machine
resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100
}


def print_report():
  # prints the amount of ingredients available in the coffee machine
  water = resources["water"]
  milk = resources["milk"]
  coffee = resources["coffee"]
  print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit}")


def is_resources_sufficient(flavor):
  # this function checks if there are sufficient resources to make the coffee

  # amount of ingredients needed to make the coffee
  water_needed = MENU[flavor]["ingredients"]["water"]
  milk_needed = MENU[flavor]["ingredients"]["milk"]
  coffee_needed = MENU[flavor]["ingredients"]["coffee"]

  # amount of ingredients remaining in the coffee machine
  water_available = resources["water"]
  milk_available = resources["milk"]
  coffee_available = resources["coffee"]

  # checks if sufficient or not, and displays the appropriate message
  if water_needed > water_available:
      print("Sorry there isn't enough water.")
      return False
  elif milk_needed > milk_available:
      print("Sorry there isn't enough milk.")
      return False
  elif coffee_needed > coffee_available:
      print("Sorry there isn't enough coffee.")
      return False
  else:
      return True


def process_coins():
  # processes the coins entered by the user and displays the total money
  print("Please insert coins.")
  quarters = int(input("How many quarters? "))
  dimes = int(input("How many dimes? "))
  nickels = int(input("How many nickels? "))
  pennies = int(input("How many pennies? "))
  total_money = (quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01)
  return total_money


should_continue = True
# if should_continue were to be false, the code would stop working i.e, the coffee machine
while should_continue:

  sufficient = False
  # takes the flavour input from the user
  flavour = input("What would you like? (espresso/latte/cappuccino) ").lower()
  # if admin inputs "off", the machine shuts down
  if flavour == "off":
      should_continue = False
      print("The machine is turning off.. Shut down.")
      break
  # if admin inputs "report", machine displays the available resources
  elif flavour == "report":
      print_report()
  # the machine checks for sufficient resources each time a flavour is chosen
  elif flavour == "latte" or flavour == "cappuccino" or flavour == "espresso":
      sufficient = is_resources_sufficient(flavour)

  if sufficient:
      total = round(process_coins(), 2)
      cost_of_coffee = MENU[flavour]["cost"]

      print(f"You entered a total of ${total}")
      if total < cost_of_coffee:
          print("Sorry that's not enough money. Money refunded.")
          continue

      elif total > cost_of_coffee:
          change = round((total - cost_of_coffee), 2)
          # change = round(change, 2)
          print(f"Here is ${change} dollars in change.")

      milk_deducted = MENU[flavour]["ingredients"]["milk"]
      water_deducted = MENU[flavour]["ingredients"]["water"]
      coffee_deducted = MENU[flavour]["ingredients"]["coffee"]

      resources["milk"] -= milk_deducted
      resources["water"] -= water_deducted
      resources["coffee"] -= coffee_deducted
      profit += total

      print(f"Here is your {flavour}. Enjoy!")
