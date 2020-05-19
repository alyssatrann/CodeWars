OPERATIONS = {
    'POWER': lambda x, y: x ** y,
    'MULTIPLY': lambda x, y: x * y,
    'DIVIDE': lambda x, y: x / y,
    'ADD': lambda x, y: x + y,
    'SUBTRACT': lambda x, y: x - y,
}

SYMBOLS = {
    'POWER': '^',
    'MULTIPLY': '*',
    'DIVIDE': '/',
    'ADD': '+',
    'SUBTRACT': '-',
}

while True:
    try:
        [a, b, op, ans] = input().split(' ')
        a = float(a)
        b = float(b)
        ans = float(ans)

        real = int(0.5 + OPERATIONS[op](a, b) * 10) / 10
        symbol = SYMBOLS[op]

        if ans != real:
            print(f'{a:.1f} {symbol} {b:.1f} = {real:.1f}, not {ans:.1f}')
        else:
            print(f'{ans:.1f} is correct for {a:.1f} {symbol} {b:.1f}')
    except EOFError:
        break
