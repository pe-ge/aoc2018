data = []
width = 0
height = 0
overlaps = set()
# with open('3a-example.txt') as f:
with open('3.txt') as f:
    for line in f.readlines():
        splitted = line.split(' ')
        pos = [int(n) for n in splitted[2][:-1].split(',')]
        dims = [int(n) for n in splitted[3].split('x')]
        data.append((pos, dims))

        width = max(width, pos[0] + dims[0] + 1)
        height = max(height, pos[1] + dims[1] + 1)

        id_cell = int(splitted[0][1:])
        overlaps.add(id_cell)

area = [[0 for _ in range(width)] for _ in range(height)]

for idx, d in enumerate(data):
    for x in range(d[0][0], d[0][0]+d[1][0]):
        for y in range(d[0][1], d[0][1]+d[1][1]):
            if area[y][x] == 0:
                area[y][x] = idx+1
            else:
                overlaps.discard(idx+1)
                overlaps.discard(area[y][x])

print(overlaps)
