from collections import Counter


def is_x2(series):
    for i in range(len(series) - 1):
        if series[i] ** 2 != series[i + 1]:
            return False
    return True


def is_x3(series):
    for i in range(len(series) - 1):
        if series[i] ** 3 != series[i + 1]:
            return False
    return True


def is_fib(series):
    for i in range(len(series) - 2):
        if series[i] + series[i + 1] != series[i + 2]:
            return False
    return True


def is_geometric_no_gaps(series):
    mult = series[1] / series[0]
    for i in range(len(series) - 1):
        if series[i] * mult != series[i + 1]:
            return False
    return True


def is_geometric_with_gaps(series):
    counter = Counter([series[i + 1] / series[i] for i in range(len(series) - 1)])
    if len(counter) > 2:
        return False
    [[_, _], [_, skip_n]] = counter.most_common(2)
    return skip_n == 1


while True:
    try:
        series = list(map(int, input().split()))

        if is_x2(series):
            print('X^2')
        elif is_x3(series):
            print('X^3')
        elif is_fib(series):
            print('Fibonacci')
        elif is_geometric_no_gaps(series):
            print('Geometric')
        elif is_geometric_with_gaps(series):
            print('Geometric (With Gaps)')
        else:
            print(' '.join(map(str, series)), 'is an Unknown series')
    except EOFError:
        break
