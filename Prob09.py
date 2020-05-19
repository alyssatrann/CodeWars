SIDE = 25 * 60
TOTAL = 2 * SIDE

while True:
    [mins, secs] = map(int, input().split(' '))
    remaining = TOTAL - mins * 60 - secs

    if remaining == TOTAL:
        break

    if remaining < 0:
        remaining = -remaining
        print(f"Time remaining {-(remaining // 60)} minutes and {-(remaining % 60)} seconds (we're gonna need a bigger record)")
    elif remaining < SIDE:
        print(f"Time remaining {remaining // 60} minutes and {remaining % 60} seconds (we'll need both sides)")
    else:
        print(f'Time remaining {remaining // 60} minutes and {remaining % 60} seconds')
