from pprint import pp


# 0 0   1 0   2 1   3 1   4 2   5 2   => 0
# p[0] 0 1 2 3 4 5
# p[1] 0 0 1 1 2 2
def convert(p):
    a = p[0]
    b = p[1] - (p[0] + p[0] % 2) // 2
    return [a, b, 0 - a - b]


[system_n, query_n] = map(int, input().split(' '))

systems = dict(
    (name, convert([int(pos[:2]), int(pos[2:])]))
    for [pos, name] in [input().split(' ') for _ in range(system_n)]
)

queries = [input().split(' ') for _ in range(query_n)]


def dist(a, b):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])) // 2


for query in queries:
    print(query[0], query[1], dist(systems[query[0]], systems[query[1]]))
