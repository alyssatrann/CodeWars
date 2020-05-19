from collections import defaultdict, namedtuple

Partial = namedtuple('Partial', 'num start len value')

h_partials = defaultdict(list)
v_partials = defaultdict(list)

while True:
    data = input()
    if data == '-------':
        break
    data = data.split(' ')

    partial_len = int(data[2])

    if data[1] == 'H':
        h_partials[int(data[4])].append(Partial(num=int(data[0]), start=int(data[3]), len=partial_len, value=[None] * partial_len))
    else:
        v_partials[int(data[3])].append(Partial(num=int(data[0]), start=int(data[4]), len=partial_len, value=[None] * partial_len))

while True:
    data = input()
    if data == '-------':
        break
    data = data.split(' ')

    x = int(data[0])
    y = int(data[1])

    if y in h_partials:
        for i in range(len(h_partials[y])):
            partial = h_partials[y][i]
            if x in range(partial.start, partial.start + partial.len):
                partial.value[x - partial.start] = data[2]
                break
    if x in v_partials:
        for i in range(len(v_partials[x])):
            partial = v_partials[x][i]
            if y in range(partial.start, partial.start + partial.len):
                partial.value[y - partial.start] = data[2]
                break

words = []

while True:
    try:
        words.append(input())
    except EOFError:
        break

partials = [p for ps in h_partials.values() for p in ps] + [p for ps in v_partials.values() for p in ps]
partials.sort(key=lambda p: p.num)


def matches(word, partial):
    for i in range(len(word)):
        if partial.value[i] is not None and word[i] != partial.value[i]:
            return False
    return True


used = set()

for partial in partials:
    for word in words:
        if len(word) != partial.len:
            continue
        if word not in used and matches(word, partial):
            print(f'{partial.num:02d} is {word}')
            used.add(word)
            break
