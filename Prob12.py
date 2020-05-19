while True:
    try:
        print(f'{sum(x * [36, 12, 1][i] for i, x in enumerate(map(int, input().split(" ")))) * 2.54:.2f}')
    except EOFError:
        break
