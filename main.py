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

# #printing report of resources
# def report():
#    return resources["water", "milk", "coffee"]

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



#checking resources if enough
def check_resources(order_ingredients):
    """returns True when order can be made or False, when NOT - ingredients insufficient"""
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f"Sorry, there is not enough of {i}.")
            return False
    return True

def check_coins():
    """returns the total money from inserted coins"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many quarters?: ")) * 0.1
    total += int(input("how many quarters?: ")) * 0.05
    total += int(input("how many quarters?: ")) * 0.01
    return total

def check_transaction_successful(money_received, drink_cost):
    """return True when the payment is accepted or false if its not enough money"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"The change: ${change}.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """updating resources"""
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name}")


state_flag = True
while state_flag:
    # ask the user what he would like
    print("Type 'report' to check resources.")
    action = input("What would you like to? Type: 'espresso', 'latte', or 'cappuccino' \n").lower()
    #printing report
    if action == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Water: {resources['milk']}ml")
        print(f"Water: {resources['coffee']}g")
        print(f"Money: {money}")
    #turning off this machine
    elif action == "off":
        print("Turning OFF")
        state_flag = False
    else:
        drink = MENU[action]
        if check_resources(drink["ingredients"]):
            payment = check_coins()
            if check_transaction_successful(payment, drink["cost"]):
                make_coffee(action, drink["ingredients"])
