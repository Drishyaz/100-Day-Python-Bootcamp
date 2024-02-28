# LIVE DEMO: https://replit.com/@guardianblossom/calculator-start#main.py
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

# Calculator
# add
def add(n1,n2):
  return n1 + n2

# subtract
def subtract(n1,n2):
  return n1 - n2

# multiply
def multiply(n1,n2):
  return n1 * n2

# divide
def divide(n1,n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  should_continue = True
  num1 = float(input("What is the first number? "))
  
  while should_continue:
    for symbol in operations:
      print(symbol)           # this will print the key
    #print(operations[sign])  # this will print the value
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the second number? "))
  
    answer = operations[operation_symbol] (num1,num2)
    # answer = function (n1, n2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    choice = input(f"Do you want to continue calculating with {answer} ? Type 'y' for yes and 'n' for no: ").lower()
    if choice == 'y':
      should_continue = True
      num1 = answer
    else:
      should_continue = False

calculator()
