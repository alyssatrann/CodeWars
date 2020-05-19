hexes = [hex(ord(letter))[2:] for letter in input() if letter != ' ']

print(' '.join(hexes))

secret = ''.join(hexes)[::-4][::-1]

print(secret)

for i in range(0, len(secret), 2):
    print(chr(int(secret[i:i+2], 16)), end='')

print()
