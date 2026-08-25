import builtins

# --- BROWSER TERMINAL FIX ---
# Save the original input so we don't accidentally create an infinite loop!
original_input = builtins.input

def instant_input(prompt_text=""):
    # Force the text to appear on the screen immediately
    print(prompt_text, end="", flush=True)
    # Call the REAL input command we saved earlier
    return original_input()

builtins.input = instant_input
# ----------------------------

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
        input("Press Enter to continue...")
        return

    drink_requirements = Menu[type_of_drink]["ingredients"]
    item_cost = Menu[type_of_drink]["cost"]

    # Step 1: Check if there are enough ingredients
    for item, amount in drink_requirements.items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item}.")
            print(f"Please refill your machine to make a {type_of_drink}!")
            input("Press Enter to continue...")
            return

    # Step 2: Ask for money
    print(f"\nA {type_of_drink} costs ${item_cost:.2f}.")
    try:
        how_many_quarters = int(input("How many quarters do you have? "))
        how_many_dimes = int(input("How many dimes do you have? "))
        how_many_nickles = int(input("How many nickles do you have? "))
        how_many_pennies = int(input("How many pennies do you have? "))
    except ValueError:
        print("Invalid coin entry. Money refunded.")
        input("Press Enter to continue...")
        return

    money_inserted = (
        (how_many_pennies * wallet['penny'])
        + (how_many_nickles * wallet['nickle'])
        + (how_many_dimes * wallet['dime'])
        + (how_many_quarters * wallet['quarter'])
    )

    # Step 3: Process the payment
    if money_inserted >= item_cost:
        calculation(type_of_drink, drink_requirements, money_inserted, item_cost)
    else:
        print("Sorry, that's not enough money. Money refunded.")
        input("Press Enter to continue...")

def calculation(type_of_drink, drink_requirements, money_inserted, item_cost):
    global profit
    for item, value in drink_requirements.items():
        resources[item] -= value
        
    profit += item_cost
    change = money_inserted - item_cost

    print(f"\nHere is your {type_of_drink} ☕. Enjoy!")
    if change > 0:
        print(f"Here is your change: ${change:.2f}")
    input("Press Enter to continue...")

is_off = False
while not is_off:
    print("----------------------------------------")
    print("Instructions:\noff - Turn off machine\nreport - View resources & profit\nrefill - Refill resources")
    print("----------------------------------------")
    choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

    if choice == "off":
        is_off = True
        print("Machine shutting down. Goodbye!")
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit:.2f}")
        input("Press Enter to continue...")
    elif choice == "refill":
        resources['water'] = 300
        resources['coffee'] = 100
        resources['milk'] = 200
        print("Resources refilled successfully!")
        input("Press Enter to continue...")
    else:
        coffee_menu(choice)
