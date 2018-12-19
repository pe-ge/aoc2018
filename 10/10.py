from math import inf
from collections import defaultdict

data = open('10.txt').read().split('\n')
# data = open('10-example.txt').read().split('\n')
points = []
for line in data:
    if not line:
        continue
    splitted = line.split('<')

    position = splitted[1].split('>')[0]
    pos_x, pos_y = map(int, position.split(','))

    velocity = splitted[2].split('>')[0]
    vel_x, vel_y = map(int, velocity.split(','))

    points.append([pos_x, pos_y, vel_x, vel_y])

move = 0
old_len = inf
while True:
    counts = defaultdict(int)
    new_points = []
    min_x, min_y, max_x, max_y = inf, inf, -inf, -inf
    for point in points:
        pos_x, pos_y, vel_x, vel_y = point

        pos_x += vel_x
        pos_y += vel_y

        new_points.append([pos_x, pos_y, vel_x, vel_y])
        counts[pos_y] += 1

        min_x = min(pos_x, min_x)
        min_y = min(pos_y, min_y)
        max_x = max(pos_x, max_x)
        max_y = max(pos_y, max_y)

    len_counts = len(counts)
    if len_counts <= old_len:
        old_len = len_counts
        points = new_points
    else:
        print(move)
        break

    move += 1

width = max_x - min_x
height = max_y - min_y

area = [['.' for _ in range(width)]for _ in range(height)]

for pos_x, pos_y, vel_x, vel_y in points:
    area[pos_y-min_y][pos_x-min_x] = '#'

for line in area:
    print(''.join(line))
