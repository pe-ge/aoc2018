data = []
width = 0
height = 0
with open('3.txt') as f:
    for line in f.readlines():
        splitted = line.split(' ')
        pos = [int(n) for n in splitted[2][:-1].split(',')]
        dims = [int(n) for n in splitted[3].split('x')]
        data.append((pos, dims))

        width = max(width, pos[0] + dims[0] + 1)
        height = max(height, pos[1] + dims[1] + 1)

area = [[0 for _ in range(width)] for _ in range(height)]

num_Xs = 0
for idx, d in enumerate(data):
    for x in range(d[0][0], d[0][0]+d[1][0]):
        for y in range(d[0][1], d[0][1]+d[1][1]):
            if area[y][x] == 0:
                area[y][x] = idx+1
            elif area[y][x] != 'X':
                area[y][x] = 'X'
                num_Xs += 1

print(num_Xs)
