Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 0.50,
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 1.00,
    },
    "cappuccino": {
        "ingredients": {
            "water": 150,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 1.50,
    },
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}

wallet = {
    "penny": 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

profit = 0


def coffee_menu(type_of_drink):
    if type_of_drink not in Menu:
        print(f"Sorry, '{type_of_drink}' is not on the menu.")
        input("Press any key to continue...")
        return

    drink_requirements = Menu[type_of_drink]["ingredients"]
    item_cost = Menu[type_of_drink]["cost"]

    for item, amount in drink_requirements.items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item}.")
            print(f"Please refill your machine to make a {type_of_drink}!")
            input("Press any key to continue...")
            return

  
    print(f"A {type_of_drink} costs ${item_cost:.2f}.")
    how_many_quarters = int(input("How many quarters do you have? "))
    how_many_dimes = int(input("How many dimes do you have? "))
    how_many_nickles = int(input("How many nickles do you have? "))
    how_many_pennies = int(input("How many pennies do you have? "))

    money_inserted = (
        (how_many_pennies * wallet['penny'])
        + (how_many_nickles * wallet['nickle'])
        + (how_many_dimes * wallet['dime'])
        + (how_many_quarters * wallet['quarter'])
    )


    if money_inserted >= item_cost:
        calculation(type_of_drink, drink_requirements, money_inserted, item_cost)
    else:
        print("Sorry, that's not enough money.")
        input("Press any key to continue...")


def calculation(type_of_drink, drink_requirements, money_inserted, item_cost):
    global profit
    print("\n" * 100)
    

    for item, value in drink_requirements.items():
        resources[item] -= value
        
    profit += item_cost
    change = money_inserted - item_cost

    print(f"Here is your {type_of_drink} ☕. Enjoy!")
    if change > 0:
        print(f"Here is your change: ${change:.2f}")
    input("Press any key to continue...")


is_off = False
while not is_off:
    print("\n" * 100)
    print(f"Instructions: \noff - turn off the machine \nreport - See your resources \nrefill - refill your resources")
    print("\n")
    choice = input("What type of coffee would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_off = True
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        input("Press any key to continue...")
    elif choice == "refill":
        resources['water'] = 300
        resources['coffee'] = 100
        resources['milk'] = 200
        print("Resources refilled successfully!")
        input("Press any key to continue...")
    else:
        coffee_menu(choice)
