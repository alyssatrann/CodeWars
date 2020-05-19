key = [
    [
        'B',
        'BB',
        'BBB',
        'BW',
        'W',
        'WB',
        'WBB',
        'WBBB',
        'BK',
    ],
    [
        'Z',
        'ZZ',
        'ZZZ',
        'ZP',
        'P',
        'PZ',
        'PZZ',
        'PZZZ',
        'ZB',
    ],
    [
        'B',
        'BB',
        'BBB',
        'BG',
        'G',
        'GB',
        'GBB',
        'GBBB',
        'BR',
    ],
    [
        'R',
    ]
]

while True:
    try:
        print(''.join(reversed([
            key[i][int(digit) - 1]
            for i, digit in enumerate(input()[::-1])
            if digit != "0"
        ])))
    except EOFError:
        break
