amounts = {
    'Pepperoni': [0, 32],
    'Red Peppers': [0, 16],
    'Pineapple': [0, 84],
    'Olives': [0, 20],
    'Sardines': [0, 12],
    'Onion': [0, 28],
    'Sausage': [0, 40],
    'Ham': [0, 36],
}


def hawaiian(count, amount=1):
    amounts['Pineapple'][0] += amount * count
    amounts['Ham'][0] += amount * count


def combo(count, amount=1):
    amounts['Red Peppers'][0] += amount * count
    amounts['Olives'][0] += amount * count
    amounts['Onion'][0] += amount * count
    amounts['Sausage'][0] += amount * count


def fishaster(count, amount=1):
    amounts['Sardines'][0] += amount * count
    amounts['Onion'][0] += amount * count


def meat_lovers(count, amount=1):
    amounts['Pepperoni'][0] += amount * count
    amounts['Sausage'][0] += amount * count
    amounts['Ham'][0] += amount * count


def cheese(count, amount=1):
    pass


premade = {
    'Hawaiian': hawaiian,
    'Combo': combo,
    'Fishaster': fishaster,
    'Meat-Lovers': meat_lovers,
    'Cheese': cheese,
}

while True:
    try:
        data = input()

        first_space_pos = data.index(' ')
        count = int(data[0:first_space_pos])

        for topping in data[first_space_pos+1:].split('&'):
            topping = topping.strip()
            space_pos = topping.find(' ')

            if space_pos == -1:  # single entry pizza
                if topping in premade:
                    premade[topping](count)
                else:
                    amounts[topping][0] += count
            else:  # with amount
                amount = eval(topping[0:space_pos])
                name = topping[space_pos+1:]
                if name in premade:
                    premade[name](count, amount)
                else:
                    amounts[name][0] += amount * count
    except EOFError:
        break

for kind, amount in amounts.items():
    print(f'{kind}: {int(amount[0] * amount[1])}')
