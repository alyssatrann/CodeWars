string_and_fret_by_note = {
    'A': '5 E 0 A 12 A',
    'B': '7 E 2 A',
    'C': '8 E 3 A',
    'D': '10 E 5 A',
    'E': '0 E 12 E 7 A',
    'F': '1 E 8 A',
    'G': '3 E 10 A',
}


next_note_by_string_and_fret = {
    'A': ['B', None, 'C', 'D', None, 'E', None, 'F', 'G', None, 'A', None, 'A'],
    'E': ['F', 'G', None, 'A', None, 'B', None, 'C', 'D', None, 'E', None, 'F'],
}

while True:
    try:
        data = input()

        if ' ' in data:
            data = data.split(' ')
            fret = int(data[0])
            string = data[1]
            print(next_note_by_string_and_fret[string][fret])
        else:
            print(string_and_fret_by_note[data])

    except EOFError:
        break
