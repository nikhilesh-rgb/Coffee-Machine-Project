MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 45.0,
    }
}

profit = 0
resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
}


def sufficient_resource(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many ₹5 coins?:  ")) * 5.0
    total += int(input("How many ₹10 coins?:  ")) * 10.0
    total += int(input("How many ₹20 coins?:  ")) * 20.0
    return total


def transaction_successful(money_given, drink_cost):
    if (money_given >=



            drink_cost):
        change = round(money_given - drink_cost, 2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is you {drink_name} enjoy :)")


is_running = True
while is_running:
    user = input("what would you like? (espresso/latte/cappuccino):  ").lower()
    if user == "off":
        is_running = False
    elif user == "report":
        print(f"Water : {resources['water']}ml.")
        print(f"Water : {resources['milk']}ml.")
        print(f"Water : {resources['coffee']}gms.")
        print(f"Money: ₹{profit}")
    else:
        drink = MENU[user]
        if sufficient_resource(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(user, drink["ingredients"])