from math import sqrt

x = int(input())


def prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if prime(x):
    print(x, "is PRIME")
else:
    print(x, "is NOT Prime")
