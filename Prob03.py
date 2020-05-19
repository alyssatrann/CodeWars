def factors(x: int):
    return set([1] + [
        m
        for n in range(2, x // 2)
        for m in [n, x // n]
        if x % n == 0
    ] + [x])


factorsX = factors(int(input()))
factorsY = factors(int(input()))

print(max(factorsX & factorsY))
