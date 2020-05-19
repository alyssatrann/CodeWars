from itertools import groupby
from pprint import pp

vowel_order = 'IAEOU'


def similar(key, check):
    return len(check) != 0 and check == ''.join(c for c in key if c in check)


def is_vowel(s, count_y=False):
    return s in vowel_order or (count_y and s == 'Y')


def vowels(word_parts):
    for is_vowels, letters in word_parts:
        if is_vowels:
            yield from letters


def list_diff(lists):
    for i in range(len(min(lists))):
        items = [list[i] for list in lists]
        if len(set(items)) > 1:
            yield from items


def vowel_diff(words):
    return ''.join(list_diff([list(vowels(word)) for word in words]))


def word_parts(word):
    no_vowels = True
    for c in word:
        if c in 'AEIOU':
            no_vowels = False
            break

    def is_vowel_maybe_y(c):
        return c in vowel_order or (no_vowels and c == 'Y')

    return [
        (is_vowels, ''.join(letters))
        for is_vowels, letters in groupby(word, is_vowel_maybe_y)
    ]


while True:
    data = input()

    if data == '0':
        break

    data = data.split()
    words_n = int(data[0])
    words = data[1:]
    words_parts = [word_parts(word) for word in words]

    print(' '.join(words), ' ', end='')
    if len(set(words)) == 1:
        print('COPY')
    elif similar(vowel_order, vowel_diff(words_parts)):
        print('PROGRESSIVE')
    elif words_n == 2 \
            and words_parts[1][0][1] == 'SHM' \
            and (words_parts[0] == words_parts[1][1:] or words_parts[0][1:] == words_parts[1][1:]):
        print('SHM')
    elif len(set([tuple(parts[1:]) for parts in words_parts])) == 1:
        print('RHYMING')
    elif len(set(
            tuple(
                ''.join(letters)
                for is_vowels, letters in parts
                if not is_vowels
            )
            for parts in words_parts
    )) == 1:
        print('ABLAUT')
    else:
        print("uh oh the program doesn't work")
