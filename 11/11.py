serial = 71
x, y = 101, 153

def get_pl(serial, x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id

    power_level = power_level // 100 % 10
    power_level -= 5

    return power_level

serial = 8979
area = [[0 for _ in range(300)] for _ in range(300)]
for x in range(300):
    for y in range(300):
        area[y][x] = get_pl(serial, x, y)

sums = []
max_s = 0
max_x = 0
max_y = 0
max_ss = 0
for ss in range(20):
    print(ss)
    for y in range(300-ss):
        for x in range(300-ss):
            s = 0
            for dy in range(ss):
                for dx in range(ss):
                    s += area[y+dy][x+dx]
            if s > max_s:
                max_s = s
                max_x = x
                max_y = y
                max_ss = ss

print(max_x, max_y, max_ss)
