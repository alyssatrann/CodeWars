def first(t):
    return t[0]


def second(t):
    return t[1]


def equal_sums(num):
    return sum(map(int, num[::-2])) == sum(map(int, num[-2::-2]))


nums = list(map(str, range(int(input()), int(input()))))
result = list(map(equal_sums, nums))

if True not in result:
    print('No Numbers found with Equal Sum in the given range!!')
else:
    print(' '.join(map(first, filter(second, zip(nums, result)))))
