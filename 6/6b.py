from pprint import pprint
coordinates = set()
width, height = 0, 0
with open('6.txt') as f:
# with open('6-example.txt') as f:
    for line in f.readlines():
        x, y = [int(n) for n in line.split(', ')]
        coordinates.add((x, y))
        width = max(x+1, width)
        height = max(y+1, height)

total_points = 0
for y in range(height):
    for x in range(width):
        total_distance = 0
        for (cx, cy) in coordinates:
            distance = abs(x-cx) + abs(y-cy)
            total_distance += distance

        if total_distance < 10000:
            total_points += 1

print(total_points)
