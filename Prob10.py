from typing import Callable


def replace_with(text: str, pattern: str, src: Callable[[], str]):
    for pos in range(len(text) - len(pattern)):
        end = pos + len(pattern)
        if text[pos:end] == pattern:
            text = text[:pos] + src() + text[end:]
    return text


def input_until(end: str):
    lines = []

    while True:
        line = input()
        if line == end:
            break
        lines.append(line)

    return lines


sentence = input()

input()

nouns = input_until('ADVERBS')
adverbs = input_until('VERBS')
verbs = input_until('ADJECTIVES')
adjectives = input_until('END')

for _ in range(2):
    mad_lib = sentence
    try:
        mad_lib = replace_with(mad_lib, '[N]', lambda: nouns.pop(0))
        mad_lib = replace_with(mad_lib, '[AV]', lambda: adverbs.pop(0))
        mad_lib = replace_with(mad_lib, '[V]', lambda: verbs.pop(0))
        mad_lib = replace_with(mad_lib, '[AJ]', lambda: adjectives.pop(0))
        print(mad_lib)
    except IndexError:
        break
