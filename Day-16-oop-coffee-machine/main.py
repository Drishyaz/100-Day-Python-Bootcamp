from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options} ")
    if choice == "off":
        print("Machine is shutting down..")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # first we find if the drink exists in the menu
        drink = menu.find_drink(choice)
        # if there are sufficient resources for the drink order made, and,
        # the machine was able to make payment
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # then we make payment
            coffee_maker.make_coffee(drink)

