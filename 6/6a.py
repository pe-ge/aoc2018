from pprint import pprint
coordinates = []
size = {}
infinite = {}
width, height = 0, 0
with open('6.txt') as f:
# with open('6-example.txt') as f:
    uid = 0
    for line in f.readlines():
        x, y = [int(n) for n in line.split(', ')]
        coordinates.append([x, y, uid, 0])
        size[uid] = 0
        infinite[uid] = False
        uid += 1
        width = max(x+1, width)
        height = max(y+1, height)

area = [['.' for _ in range(width)] for _ in range(height)]
# pprint(area)


def floodfill():
    while coordinates:
        x, y, uid, level = coordinates.pop(0)
        if x < 0 or y < 0 or x >= width or y >= height:
            infinite[uid] = True
            continue

        if area[y][x] == '.':
            area[y][x] = [uid, level]
            size[uid] += 1

            # add neighbors to coordinates
            for dx, dy in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            # for dx, dy in ([1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]):
                coordinates.append([x+dx, y+dy, uid, level+1])
        else:
            if area[y][x][1] == level and area[y][x][0] != uid and area[y][x][0] != '.':
                size[area[y][x][0]] -= 1
                area[y][x][0] = '.'

floodfill()
# for row in area:
    # for [uid, level] in row:
        # print(uid, end='')
    # print()

max_area = 0
for k, v in size.items():
    if not infinite[k]:
        max_area = max(max_area, v)
# print(size)

# print(infinite)
print(max_area)
