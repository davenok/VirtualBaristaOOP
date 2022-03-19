from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

running = True

print("CoffeeOS initializing...")
print("Saving the world, one coffee bean at a time!")
print("heating up the water")
sleep(2)
print("grinding the beans\n\n")
sleep(2)

while running:
    print(my_menu.get_items())
    order = input("What would you like? ")
    if order == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif order == "off" or order == "quit":
        running = False
    else:
        item = my_menu.find_drink(order)
        if item:
            if my_coffee_maker.is_resource_sufficient(item):
                print("That will be " + str(item.cost))
                if(my_money_machine.make_payment(item.cost)):
                    my_coffee_maker.make_coffee(item)
    print("\n\n")