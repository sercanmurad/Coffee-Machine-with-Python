MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "sugar": 4,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
            "sugar": 7,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
            "sugar": 5,
        },
        "cost": 3.0,

    },
    "tea":{
        "ingredients":{
            "water":160,
            "milk":0,
            "coffee":0,
            "sugar":3,
        },
        "cost":2.0
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "sugar": 10,
}


#TODO 1-Print report of coffee machine items-checked
#TODO 2-Check resources sufficient to our chosen drink
#TODO 3-Procces coins
#TODO 4-Check transaction succesfull
#TODO 5-Make coffe-increase resources and add money to machine resoources

profit=0


def resource_sufficient(order_incredient):
    """Returns True when order can be made, False if our resources are insufficient."""
    is_enough = True
    for item in order_incredient:
       if order_incredient[item]>=resources[item]:
           print(f"Sorry there is not enough {item}!!!")
           is_enough = False
    return is_enough

def is_transaction_successsful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        changed=round(money_received-drink_cost, 2)
        print(f"Here is ${changed} in  changed.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not eneough.Money refunded. ")
        return False


def make_coffee(drink_name, order_ingredients):
    """Increase the required ingredients from the starter resources."""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}☕.")


def proces_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total  =int(input("How many quarters:")) * 0.25
    total +=int(input("How many dimes: ")) * 0.10
    total +=int(input("How many nickles")) * 0.05
    total +=int(input("How many pennies:")) * 0.01
    return total
is_work= True

while is_work:
    order=input("What would you like? (espresso/latte/cappuccino/tea):")
    if order == "off":
        is_work=False
    elif order == "report":
        print(f"Water:{resources['water']} ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Sugar: {resources['sugar']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[order]
        if resource_sufficient(drink["ingredients"]):
            payment = proces_coins()
            if is_transaction_successsful(payment, drink["cost"]):
                make_coffee(order,  drink["ingredients"])