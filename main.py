MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 4: Check resources sufficient?
def check_resources():
    for key in resources:
        MENU[prompt]['ingredients'].setdefault(key)
        if MENU[prompt]['ingredients'][key] is not None and MENU[prompt]['ingredients'][key] > resources[key]:
            not_enough = key
            return not_enough
    return True


# TODO 5: Process coins.
def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) * (pennies * 0.01)
    return total


# TODO 7: Make Coffee.
def make_coffee():
    for key in resources:
        MENU[prompt]['ingredients'].setdefault(key)
        if MENU[prompt]['ingredients'][key] is not None:
            resources[key] -= MENU[prompt]['ingredients'][key]
    return f"Here is your {prompt}. ☕ Enjoy!"


machine_running = True
resources['cost'] = 0

while machine_running:
    # TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt.
    if prompt == 'off':
        machine_running = False
    # TODO 3: Print report.
    elif prompt == 'report':
        print(
            f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${'{:.2f}'.format(resources['cost'])}")
    else:
        if check_resources() == True:
            total_coins = process_coins()
            # TODO 6: Check transaction successful?
            if total_coins < MENU[prompt]['cost']:
                print("Sorry that's not enough money. Money refunded.")
            elif total_coins > MENU[prompt]['cost']:
                change = total_coins - MENU[prompt]['cost']
                resources['cost'] += MENU[prompt]['cost']
                print(f"Here is ${'{:.2f}'.format(change)} in change.")
                print(make_coffee())
            elif total_coins == MENU[prompt]['cost']:
                resources['cost'] += total_coins
                print(make_coffee())
        else:
            print(f"Sorry there is not enough {check_resources()}.")
