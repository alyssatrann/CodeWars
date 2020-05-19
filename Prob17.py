from collections import defaultdict

city_n = int(input())

cities = dict((input(), i) for i in range(city_n))

connections = defaultdict(set)

while True:
    try:
        data = input().split(' ')
        a = data[1]
        b = data[6]

        if data[8] != "air":
            connections[a].add(b)
            connections[b].add(a)
    except EOFError:
        break

for city in cities.keys():
    neighbours = set()
    new_connections = {city}
    while len(new_connections) != 0:
        new_new_connections = set()
        for connection in new_connections:
            neighbours.add(connection)
            new_new_connections |= connections[connection]
        new_connections = new_new_connections - neighbours
    neighbours -= {city}
    if len(neighbours) == 0:
        print(f'City {city} is remote and has no neighbours!')
    else:
        print(f'City {city} is neighbour to Cities {",".join(sorted(neighbours, key=lambda n: cities[n]))}')
