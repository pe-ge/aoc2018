import numpy as np
from PIL import Image, ImageDraw

class Main:
    def __init__(self, filename):
        self.min_x = 999999
        self.max_x = 0
        self.max_y = 0

        data = open(filename).read().split('\n')

        clay = []
        for line in data:
            if not line:
                continue

            line = line.split(', ')

            first_coor, first_val = line[0].split('=')
            first_val = int(first_val)
            if first_coor == 'x':
                self.min_x = min(self.min_x, first_val)
                self.max_x = max(self.max_x, first_val)
                x = (first_val, first_val)
            else:
                self.max_y = max(self.max_y, first_val)
                y = (first_val, first_val)

            second_coor = line[1].split('=')
            vals = tuple(map(int, second_coor[1].split('..')))
            if second_coor[0] == 'x':
                x = vals
                self.min_x = min(self.min_x, x[0])
                self.max_x = max(self.max_x, x[1])
            else:
                y = vals
                max_y = max(self.max_y, y[1])

            clay.append((x, y))

        self.width = self.max_x - self.min_x + 2
        self.height = max_y + 1
        self.ground = [['.' for _ in range(self.width)] for _ in range(self.height)]

        # water
        self.ground[0][500-self.min_x] = '+'
        self.water_pos = {(500, 0): (True, False)}  # (x, y) => (alive, hit ground)
        self.total_water = 0

        # clay
        for (xs, ys) in clay:
            for x in range(xs[0], xs[1]+1):
                for y in range(ys[0], ys[1]+1):
                    self.set(x, y, '#')

    def print(self):
        for row in self.ground:
            print(''.join(row))

    def to_image(self, filename):
        symbols = {
            '.': [255, 255, 255],
            '+': [0, 0, 255],
            '~': [120, 120, 255],
            '#': [0, 0, 0]
        }

        data = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        for row_idx, row in enumerate(self.ground):
            for col_idx, char in enumerate(row):
                data[row_idx, col_idx] = symbols[char]

        img = Image.fromarray(data, 'RGB')
        draw = ImageDraw.Draw(img)
        idx = 0
        for (water_x, water_y), (alive, hit_ground) in self.water_pos.items():
            draw.text((10, 10 * idx), '%d %d %s %s' % (water_x, water_y, str(alive), str(hit_ground)), (0, 0, 0))
            idx += 1
        img.save(filename)

    def set(self, x, y, symbol):
        if self.get(x, y) != '~' and symbol == '~':
            self.total_water += 1
        self.ground[y][x-self.min_x] = symbol

    def get(self, x, y):
        return self.ground[y][x-self.min_x]

    def fill(self, water_x, water_y, dx):
        x, y = water_x, water_y
        while True:
            if x - self.min_x >= self.width or x - self.min_x < 0:
                return None, None

            symbol = self.get(x, y)


            # if already water and another water source exists => delete it
            if symbol == '~' and (x, y) in self.water_pos and (x != water_x or y != water_y):
                self.water_pos[(x, y)] = (False, False)
                return None, None

            # if already water and another water source exists => delete it
            if symbol == '~' and (x, y-1) in self.water_pos and (x != water_x or y != water_y):
                self.water_pos[(x, y-1)] = (False, False)
                return None, None

            # if already water and another water source exists => delete it
            if symbol == '~' and (x, y-2) in self.water_pos and (x != water_x or y != water_y):
                self.water_pos[(x, y-2)] = (False, False)
                return None, None

            # if free => fill with water
            if symbol == '.':
                self.set(x, y, '~')

            # if free below => stop and return new water source
            if self.get(x, y+1) == '.':
                return x, y

            # if wall hit => stop
            if self.get(x, y) == '#':
                return None, None

            x += dx

    def can_fall(self, water_x, water_y, dx):
        while True:
            symbol_current = self.get(water_x, water_y)
            symbol_below = self.get(water_x, water_y + 1)

            if symbol_below in ('.'):
                return True

            if symbol_current == '#':
                return False

            water_x += dx

    def one_step(self):
        # store water positions
        water_pos = self.water_pos
        self.water_pos = {}
        for (water_x, water_y), (alive, hit_ground) in water_pos.items():
            if not alive or water_y is None or water_x is None:
                continue
            # if falling off map
            if water_y+1 == self.height:
                continue

            symbol_below = self.get(water_x, water_y+1)
            # if empty below => falling
            if symbol_below == '.':
                self.set(water_x, water_y+1, '~')
                self.water_pos[(water_x, water_y+1)] = (True, False)
                continue

            # if wall below => filling
            if symbol_below == '#':
                # fill left
                nx1, ny1 = self.fill(water_x, water_y, -1)
                # fill right
                nx2, ny2 = self.fill(water_x, water_y, 1)

                # leaving borders
                if nx1 or nx2:
                    if nx1:
                        self.water_pos[(nx1, ny1)] = (True, False)
                    if nx2:
                        self.water_pos[(nx2, ny2)] = (True, False)
                else:
                    self.water_pos[(water_x, water_y-1)] = (True, True)

            if symbol_below == '~':
                if hit_ground:
                    # fill left
                    nx1, ny1 = self.fill(water_x, water_y, -1)
                    # fill right
                    nx2, ny2 = self.fill(water_x, water_y, 1)

                    # leaving borders
                    if nx1 or nx2:
                        if nx1:
                            self.water_pos[(nx1, ny1)] = (True, False)
                        if nx2:
                            self.water_pos[(nx2, ny2)] = (True, False)
                    else:
                        self.water_pos[(water_x, water_y-1)] = (True, True)
                else:
                    # check for falling left
                    if self.can_fall(water_x, water_y, -1):
                        pass
                    # falling right
                    elif self.can_fall(water_x, water_y, 1):
                        pass
                    else:
                        self.water_pos[(water_x, water_y)] = (True, True)

if __name__ == '__main__':
    # m = Main('17e.txt')
    m = Main('17.txt')
    steps = 1
    while m.water_pos:
        print(steps)
        m.one_step()
        # if steps > 2600 and steps < 2700:
        # if steps % 100 == 0:
            # m.to_image('imgs/%d.png' % steps)
        steps += 1

    chybajuce = 74
    navyse = 9
    print(m.total_water + chybajuce - navyse)
    m.to_image('imgs/final.png')
