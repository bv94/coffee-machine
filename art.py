import re
storage = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
recipes = {
    'espresso': {
        "water": 50,
        "milk": 0,
        "coffee": 18,
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
    },
    "cappucino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
    },
}
coins = {
    "penny": 0.01,
    "nickel": 0.05,

    "dime": 0.1,
    "quarter": 0.25
}
cost = {
    "espresso": 1.5,
    "latte": 2.5,
    "cappucino": 3.0
}


def can_operate():
    can_make = []
    for recipe in recipes:
        if recipes[recipe]['water'] <= storage['water'] and recipes[recipe]["coffee"] <= storage['coffee'] and recipes[recipe]["milk"] <= storage['milk']:
            can_make.append(recipe)

    return can_make


def coin_counter(coin):
    lst = re.split('p|n|d|q', coin)
    lst.pop(len(lst)-1)
    # lst[len(lst)-1] = strip(lst[len(lst)-1])
    print(lst)
    for i in range(4):
        lst[i] = float(((lst[i])))*coins[list(coins.keys())[i]]

    return sum(lst)


def prepare(type):
    global storage
    for incrediant in recipes[type]:
        storage[incrediant] -= recipes[type][incrediant]


def refill(water, milk, coffee):
    global storage
    storage['water'] += water
    storage['milk'] += milk
    storage['coffee'] += coffee


def operate():
    _ = input("what would you like?")
    if _ == 'refill':
        _ = input('how much would you like to refill\n')
        _ = _.strip().split(',')
        print(_)
        for i in range(3):
            _[i] = int(_[i])

        refill(_[0], _[1], _[2])

        operate()

    menus = can_operate()
    if len(menus) == 0:
        _ = input("out of order\n>")
        operate()
    menu = ''
    for item in menus:
        menu += ' ' + item

    query = int(input(f'what kind of coffee do you want?\n we have {menu}\n>'))
    query = menus[query-1]
    print(f"that will be {cost[query]}$")
    paid = coin_counter(input('>'))
    if paid < cost[query]:
        print("that's not sufficient\nhere is the refund")
        operate()

    prepare(query)
    change = paid - cost[query]
    print(
        f"here is your {query}\nthanks for using me\n here is your change {change}$")
    operate()


# def refill(refill):
#     refill = re.split('refill|Refill|REFILL', refill)
#     return refill
operate()
