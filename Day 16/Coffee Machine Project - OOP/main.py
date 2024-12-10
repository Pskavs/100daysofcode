from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creates objects to accomplish code requirements.
user_item = MenuItem
coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#Function has each of the objects that were created above.
def main(u_item, c_menu, c_maker, m_machine):
    u_item.__name__ = input(f"What would you like? {c_menu.get_items()} : ").lower()

    #prints a report of profits and ingredients left in the machine or turns off the machine
    if u_item.__name__ == "report":
        print(c_maker.report(), m_machine.report())
        main(u_item, c_menu, c_maker, m_machine)
    elif u_item.__name__ == "off":
        print("Powering off...")
        exit()

    u_item = c_menu.find_drink(u_item.__name__)
    print(u_item.cost)
    #Checks if the user inputted an actual drink. Then checks to see if there are enough resources
    if u_item is not None:
        if c_maker.is_resource_sufficient(u_item) is True:
            if m_machine.make_payment(u_item.cost) is True:
                c_maker.make_coffee(u_item)
    make_more = ''
    #Checks to see if the user wants to brew more coffee.

    while make_more not in ["y", "n"]:
        make_more = input("Make another coffee? y/n:").lower()
        if make_more == "y":
            main(u_item,c_menu, c_maker, m_machine)
        elif make_more == "n":
            print("Thank you for using Coffee Maker!")
            exit()
main(user_item,coffee_menu,coffee_maker,money_machine)