MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}


def display_report():
    return f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${resources['money']}"


def check_resources(coffee):
    ingredient = ['water', 'milk', 'coffee']
    for i in ingredient:
        if resources[i] >= MENU[coffee]["ingredients"][i]:
            return True
        else:
            return False


def update_resources(coffee):
    ingredient = ['water', 'milk', 'coffee']
    for i in ingredient:
        resources[i] -= MENU[coffee]["ingredients"][i]
    resources["money"] += MENU[coffee]["cost"]


def machine():
    machine_working = True
    while machine_working:
        cof = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        if cof == "report":
            print(display_report())
        else:
            if check_resources(cof):
                print("Please insert coins.")
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickels = int(input("How many nickels? "))
                pennies = int(input("How many pennies? "))
                total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
                if total == MENU[cof]['cost']:
                    update_resources(cof)
                    print(f"Here is your {cof.title()} ☕. Enjoy!")
                elif total > MENU[cof]['cost']:
                    update_resources(cof)
                    print(
                        f"Here is ${round(total - MENU[cof]['cost'], 2)} in change.\nHere is your {cof.title()} ☕. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")


machine()


# TODO: 1. Print report.

# TODO: 2. Check if the resources are sufficient.

# TODO: 3. Process coins.

# TODO: 4. Check if transaction was successful.

# TODO: 5. Make coffee.
