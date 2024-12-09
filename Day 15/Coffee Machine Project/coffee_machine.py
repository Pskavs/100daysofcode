#Sets up the resources
import coffee_machine_art
MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "milk": 0,
                "coffee": 18,
            },
            "cost": 1.50,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.50,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.00,
        }
    }

resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        'money':0,
    }

def main():
    def coffee_prompt():
        """Asks the users what drink they would like to make."""
        print(coffee_machine_art.logo)
        user_input = ''
        while user_input not in ["espresso", "latte", "cappuccino"]:
            user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
            if user_input == 'off':
                turn_off()
            if user_input == 'report':
                report()
        return user_input
    def turn_off():
        """Turns off the machine."""
        print("Turning off...")
        exit()

    def report():
        """Prints a report of all the levels in resources."""
        print(f"Water: {resources["water"]}ml\n"
              f"Milk: {resources["milk"]}ml\n"
              f"Coffee: {resources["coffee"]}g\n"
              f"Money: ${resources['money']:.2f}")

    def check_resources(u_input):
        """Checks to make sure there are enough of each resource to make the drinks."""
        water_needed = MENU[u_input]["ingredients"]["water"]
        milk_needed = MENU[u_input]["ingredients"]["milk"]
        coffee_needed = MENU[u_input]["ingredients"]["coffee"]
        if water_needed > resources["water"]:
            print("Not enough water in machine. Please add more.")
            exit()
        if milk_needed > resources["milk"]:
            print("Not enough milk in machine. Please add more.")
            exit()
        if coffee_needed > resources["coffee"]:
            print("Not enough coffee in machine. Please add more.")
            exit()
        else:
            process_payment(u_input)

    def process_payment(u_input):
        """Asks the users to enter money, one value at a time. Similar to a vending machine. It then calculates
        the total amount entered. """
        dollars = 0
        quarters = 0
        dimes = 0
        nickles = 0
        pennies = 0
        total_money = 0
        print(f"The selection costs ${MENU[u_input]['cost']:.2f}")
        numeric_value = False
        while numeric_value is not True:
            try:
                dollars = int(input("Enter dollars: "))
                quarters = int(input("Enter quarters: "))
                dimes = int(input("Enter dimes: "))
                nickles = int(input("Enter nickles: "))
                pennies = int(input("Enter pennies: "))
                numeric_value = True
            except ValueError:
                print("Please enter whole numbers.")

        total_money = round(dollars + (0.25*quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 *pennies),2)
        check_transaction(total_money, u_input)

    def check_transaction(t_money, u_input):
        """Checks to see if the user put in enough money."""
        change = 0.00
        if t_money >= MENU[u_input]['cost']:
            print("Thank you for your payment, dispensing drink now...")
            change = t_money - MENU[u_input]['cost']
            resources['money'] += MENU[u_input]['cost']
            make_coffee(u_input)
        else:
            print("Amount insufficient. Dispensing change.")
            change = t_money
        print(f"Change: ${change:.2f}")

    def make_coffee(u_input):
        """Uses the resources to make coffee and tells the user to enjoy"""
        resources["coffee"] -= MENU[u_input]['ingredients']['coffee']
        resources["water"] -= MENU[u_input]['ingredients']['water']
        resources["milk"] -= MENU[u_input]['ingredients']['milk']
        print(f"Enjoy your {u_input}!")


    #Function Calls
    user_input = coffee_prompt()
    check_resources(user_input)
    make_another =''

    #Sees if the user wants to make another coffee.
    while make_another is not ['y','n']:
        make_another = input("Would you like to make another drink? (y/n): ").lower()
        if make_another == 'y':
            main()
        elif make_another == 'n':
            print("Thank you for using CoffeeMachine!")
        elif make_another == 'off':
            turn_off()
        elif make_another == 'report':
            report()
main()