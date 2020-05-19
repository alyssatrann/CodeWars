from datetime import datetime, timedelta
from pprint import pp

DAYS = timedelta(days=1)
HOURS = timedelta(hours=1)
MINS = timedelta(minutes=1)

queries: [datetime, datetime, set] = []

while True:
    try:
        parts = input().split()

        queries.append([
            datetime(*map(int, parts[0].split('-') + parts[1].split(':'))),
            datetime(*map(int, parts[2].split('-') + parts[3].split(':'))),
            set(parts[4]),
        ])
    except EOFError:
        break


for query in queries:
    print('there are ', end='')
    diff = query[1] - query[0]
    if 'D' in query[2]:
        days = diff // DAYS
        print(int(days), 'days', end=' ')
        diff -= timedelta(days=days)
    if 'H' in query[2]:
        hours = diff // HOURS
        print(int(hours), 'hours', end=' ')
        diff -= timedelta(hours=hours)
    if 'M' in query[2]:
        mins = diff // MINS
        print(int(mins), 'minutes', end=' ')
        diff -= timedelta(minutes=mins)
    if 'S' in query[2]:
        print(int(diff.total_seconds()), 'seconds', end=' ')
    print(f'remaining until {query[1].year:04d}-{query[1].month:02d}-{query[1].day:02d} {query[1].hour:02d}:{query[1].minute:02d}:{query[1].second:02d}')
