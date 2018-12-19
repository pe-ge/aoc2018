from sortedcontainers import SortedDict
from copy import deepcopy


class Main:
    def __init__(self, filename):
        # init structures
        self.map = []
        self.units = SortedDict()
        self.enemies = {'G': 'E', 'E': 'G'}

        self.num_elves = 0

        # read input from file
        data = open(filename).read().split('\n')
        for row_idx, row in enumerate(data):
            if row == '':
                break
            self.map.append(['.'] * len(row))
            for col_idx, char in enumerate(row):
                if char in ('E', 'G'):
                    self.units[self.hash_rowcol(row_idx, col_idx)] = {
                        'type': char,
                        'HP': 200,
                        'attack_power': 3
                    }
                    if char == 'E':
                        self.num_elves += 1
                else:
                    self.map[row_idx][col_idx] = char

    def hash_rowcol(self, row, col):
        return row * 1000 + col

    def unhash_rowcol(self, hashed_rowcol):
        return hashed_rowcol // 1000, hashed_rowcol % 1000

    def neighbors(self, hashed_rowcol):
        return [
            hashed_rowcol - 1000,  # top
            hashed_rowcol - 1,  # left
            hashed_rowcol + 1,  # right
            hashed_rowcol + 1000  # bottom
        ]

    def print_map(self):
        for row_idx, row in enumerate(self.map):
            units = []
            # print map
            for col_idx, char in enumerate(row):
                hashed_rowcol = self.hash_rowcol(row_idx, col_idx)
                if hashed_rowcol in self.units:
                    print(self.units[hashed_rowcol]['type'], end='')
                    units.append(self.units[hashed_rowcol])
                else:
                    print(char, end='')

            # print units
            if units:
                print(' ' * 3, end='')
            for unit in units:
                print('{type}{HP}, '.format(**unit), end='')

            print()

    def find_nearest(self, init_hashed_rowcol):
        unit = self.units[init_hashed_rowcol]
        enemy = self.enemies[unit['type']]

        to_explore = [init_hashed_rowcol]
        visited = set()
        paths = {}
        found = False
        while to_explore and not found:
            hashed_rowcol = to_explore.pop(0)

            neighbors = self.neighbors(hashed_rowcol)
            for neighbor in neighbors:
                if neighbor in self.units and self.units[neighbor]['type'] == enemy:
                    # store path to target
                    paths[neighbor] = hashed_rowcol

                    # break while loop
                    found = True
                    break
                else:
                    # mark empty nodes to be explored
                    row_idx, col_idx = self.unhash_rowcol(neighbor)
                    if self.map[row_idx][col_idx] == '.' and neighbor not in self.units and neighbor not in visited:
                        visited.add(neighbor)
                        paths[neighbor] = hashed_rowcol
                        to_explore.append(neighbor)

        # if solution not found, return same node
        if not found:
            return init_hashed_rowcol

        # obtain path by traversing backwards
        path = [neighbor, hashed_rowcol]
        while hashed_rowcol != init_hashed_rowcol:
            hashed_rowcol = paths[hashed_rowcol]
            path.append(hashed_rowcol)

        # if already adjacent to target
        if len(path) == 2:
            return init_hashed_rowcol

        # return node to move to
        return path[-2]

    def one_round(self):
        unit_hashes = list(self.units.keys())
        for unit in unit_hashes:
            if unit not in self.units:
                continue
            attribs = self.units[unit]

            nearest = self.find_nearest(unit)
            # remove old position
            del self.units[unit]
            # move to new
            self.units[nearest] = attribs
            unit = nearest

            # attack weakest neighbor if exists
            enemy = self.enemies[attribs['type']]
            weakest_neighbor = None
            weakest_neighbor_HP = 99999
            neighbors = self.neighbors(unit)
            for neighbor in neighbors:
                if neighbor in self.units and self.units[neighbor]['type'] == enemy:
                    neighbor_HP = self.units[neighbor]['HP']
                    if neighbor_HP < weakest_neighbor_HP:
                        weakest_neighbor_HP = neighbor_HP
                        weakest_neighbor = neighbor
            if weakest_neighbor:
                self.units[weakest_neighbor]['HP'] -= attribs['attack_power']
                # check for dead unit
                if self.units[weakest_neighbor]['HP'] <= 0:
                    if self.units[weakest_neighbor]['type'] == 'E':
                        self.num_elves -= 1
                    del self.units[weakest_neighbor]


    def any_team_dead(self):
        teams = set()
        for unit, attribs in self.units.items():
            teams.add(attribs['type'])
            if len(teams) == 2:
                return False
        return True

    def goblins_dead(self):
        for unit, attribs in self.units.items():
            if attribs['type'] == 'G':
                return False
        return True

    def count_winner_hp(self):
        total_sum = 0
        for unit, attribs in self.units.items():
            total_sum += attribs['HP']
        return total_sum


if __name__ == '__main__':
    m = Main('15.txt')

    attack_power = 2
    while True:
        print('joo')
        attack_power += 1
        m_copy = deepcopy(m)
        # inc attack power
        for unit, attribs in m_copy.units.items():
            if attribs['type'] == 'E':
                attribs['attack_power'] = attack_power

        # simulate attacks
        round = 0
        while not m_copy.any_team_dead():
            round += 1
            print('After', round, 'round:')
            m_copy.one_round()
            m_copy.print_map()

        if m_copy.goblins_dead() and m.num_elves == m_copy.num_elves:
            print((round-1) * m_copy.count_winner_hp())
            print((round) * m_copy.count_winner_hp())
            break
