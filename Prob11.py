def cyclops(num):
    binary = bin(num)[2:]  # skip 0b

    if len(binary) % 2 == 0:
        return False

    mid = len(binary) // 2

    return binary[mid] == '0' and '0' not in (binary[:mid] + binary[mid+1:])


while True:
    try:
        num = int(input())

        print(num, 'yes' if cyclops(num) else 'no')
    except EOFError:
        break
