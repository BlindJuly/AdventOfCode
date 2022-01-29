

with open('movements_Dive.txt') as f:
    moves = f.readlines()

print(moves)

count_v = 0
count_h = 0
for move in moves:
    if len(move) == 7:
        count_v += int(move[5])
    elif len(move) == 10:
        count_h += int(move[8])
    else:
        count_v -= int(move[3])

print(count_h * count_v)