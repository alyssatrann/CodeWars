key = {
    frozenset({'RED', 'YELLOW'}): 'ORANGE',
    frozenset({'RED', 'BLUE'}): 'PURPLE',
    frozenset({'RED'}): 'RED',
    frozenset({'YELLOW', 'BLUE'}): 'GREEN',
    frozenset({'YELLOW'}): 'YELLOW',
    frozenset({'BLUE'}): 'BLUE',
}

while True:
    try:
        colors = frozenset(input().split(' '))

        if 'BLACK' in colors:
            if len(colors) == 1:
                print('BLACK')
            else:
                (other,) = colors - {'BLACK'}
                print(f'DARK {other}')
        elif 'WHITE' in colors:
            if len(colors) == 1:
                print('WHITE')
            else:
                (other,) = colors - {'WHITE'}
                print(f'LIGHT {other}')
        else:
            print(key[colors])
    except EOFError:
        break
