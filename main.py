#TODO 0: Establish a menu and have resources set.
Menu = {
    "expresso": {
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    },
}
profit = 0
resources = {
        "water": 300,
        "coffee": 100,
        "milk": 200,
}

def is_valid_amount(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
             print(f"Sorry there is not enough {item}.")
             is_enough = False
        return is_enough

def coffee(drink_from_menu, order_ingredients):
    '''Decuting the ingredients'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_from_menu}")

def coins():
    print("Please insert number of coins (penny, dime, nickel, or quarter)\n The max amount the machine can take is 10 of any coins:")
    # The following determines the type of coins inserted
    penny = int(input("How many penny: "))
    dime = int(input("How many dime: "))
    nickel = int(input("How many nickel: "))
    quarter = int(input("How many quarters: "))
    if penny <= 10 and dime <= 10 and nickel <= 10 and quarter <= 10:
        # The following determines the value of the coins
        valpenny = 0.01
        valdime = 0.10
        valnickel = 0.05
        valquarter = 0.25

        # Now we will calculate the value of the total money inserted by doing the multiplication between (value * number) of coins
        money = (valquarter * quarter) + (valnickel * nickel) + (valdime * dime) + (valpenny * penny)
        # money = '$' + money
        return money
    else:
        print("Invalid transaction you have inserted more than 10 coins for one or more type. Your money is refunded")



def transaction_successful(money_inserted, drink_cost):
    ''''Return true when the payment is accepted or false if money is insufficient'''
    if money_inserted >= drink_cost:
        change = round(money_inserted - drink_cost, 2)
        print(f"Here is your change, ${change}!")
        global profit
        profit += drink_cost
        return True
    else:
        print(f'Not enough money, here is your refund!')
        return False

is_on = True
#TODO 1 Ask the user for their coffee choice and get the money.
while is_on:
    coffee_consumed = input(f"Choose a coffee, your option is: expresso, latte, cappuccino or report: ") #Asking the user for their choice
    if coffee_consumed == "off":
        is_on = False
        print("The coffee machine is turned off, come back later!")

#TODO 2 : print the report of all the ingredients. # this allows us to get the input from the user to collect information to produce the output.
    elif coffee_consumed == 'report': #If the coffee machine is turned on
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money:${profit}")
    elif coffee_consumed != "report" and is_on == True:
        #We have to ask for money to continue the process
        drink = Menu[coffee_consumed]
        if is_valid_amount(drink["ingredients"]):
            money = coins()
            if transaction_successful(money, drink["cost"]):
                coffee(coffee_consumed, drink["ingredients"])