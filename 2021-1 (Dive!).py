

with open('movements_Dive.txt') as f:
    moves = f.readlines()

print(moves)

count_v = 0
count_h = 0
for move in moves:
    check_char = move[0]
    if check_char == 'd':
        count_v += int(move[5])
    elif check_char == 'f':
        count_h += int(move[8])
    else:
        count_v -= int(move[3])

print(count_h * count_v)