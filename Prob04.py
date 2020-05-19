from math import gcd


def lcm(x, y):
    return abs(x * y) // gcd(x, y)


print(lcm(int(input()), int(input())))
