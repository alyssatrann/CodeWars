[money, item_count] = map(int, input().split(' '))

items = []

for i in range(item_count):
    [name, cost] = input().split(' ')
    items.append([name, int(cost)])

items.sort(key=(lambda x: x[1]))

afford = [False for _ in items]

for i, [name, cost] in enumerate(items):
    if cost <= money:
        afford[i] = True
        money -= cost

any = False

for [name, _], can in zip(items, afford):
    if can:
        any = True
        print(f'I can afford {name}')
    else:
        print(f"I can't afford {name}")

if not any:
    print('I need more Yen!')

print(money)
