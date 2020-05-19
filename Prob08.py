from math import ceil


def wrap(s: str):
    line_count = ceil(len(s) / 80)
    split = 0
    pos = 80

    while pos < len(s) and split < line_count:
        while s[pos] != ' ':
            pos -= 1
        s = s[:pos] + '\n' + s[pos + 1:]
        split += 1
        pos += 81  # skip \n again

    return s


while True:
    try:
        print(wrap(input()))
    except EOFError:
        break
