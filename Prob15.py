while True:
    [a_len, b_len] = map(int, input().split(' '))

    if a_len == 0 and b_len == 0:
        break

    a = input()
    b = input()

    a_set = set(a.lower().split(' '))
    b_set = set(b.lower().split(' '))

    dupes = a_set & b_set

    print(a)
    print(b)
    print(len(dupes), ' '.join(dupes))
