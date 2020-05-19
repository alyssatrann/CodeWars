from collections import defaultdict

rotated = defaultdict(lambda: None)
rotated["a"] = "e"
rotated["b"] = "q"
rotated["d"] = "p"
rotated["h"] = "y"
rotated["m"] = "w"
rotated["n"] = "u"
rotated["e"] = "a"
rotated["q"] = "b"
rotated["p"] = "d"
rotated["y"] = "h"
rotated["w"] = "m"
rotated["u"] = "n"
rotated["o"] = "o"
rotated["s"] = "s"
rotated["x"] = "x"
rotated["z"] = "z"


def valid(s):
    s = [c for c in s if c != ' ']
    for i in range(len(s) // 2):
        if s[i] != rotated[s[~i]]:
            return False
    return True


for _ in range(int(input())):
    text = ''.join(c for c in input().lower() if c.isalpha() or c == ' ')
    print(f'{text} ({"is" if valid(text) else "not"})')
