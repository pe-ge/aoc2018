from collections import defaultdict

acres = list(map(list, open('18.txt').read().split('\n')))[:-1]
# acres = list(map(list, open('18e.txt').read().split('\n')))[:-1]

def around(acres, row, col):
    result = {'.': 0, '#': 0, '|': 0}
    for r in [row-1, row, row+1]:
        for c in [col-1, col, col+1]:
            if (r == row and c == col) or r < 0 or c < 0 or r >= len(acres) or c >= len(acres[0]):
                continue
            result[acres[r][c]] += 1
    return result

def one_minute(acres):
    new_acres = []
    for row_idx, row in enumerate(acres):
        new_row = []
        for col_idx, char in enumerate(row):
            fields_around = around(acres, row_idx, col_idx)
            if char == '.':
                if fields_around['|'] >= 3:
                    new_row.append('|')
                else:
                    new_row.append('.')
                continue

            if char == '|':
                if fields_around['#'] >= 3:
                    new_row.append('#')
                else:
                    new_row.append('|')
                continue

            if char == '#':
                if fields_around['#'] >= 1 and fields_around['|'] >= 1:
                    new_row.append('#')
                else:
                    new_row.append('.')
        new_acres.append(new_row)

    return new_acres

def print_acres(acres):
    for row in acres:
        print(''.join(row))
    print()

def count_total(acres):
    result = {'.': 0, '#': 0, '|': 0}
    for row in acres:
        for char in row:
            result[char] += 1
    return result
# print('init')
# print_acres(acres)
# totals = defaultdict(int)
# for i in range(1200):
    # print(i)
    # acres = one_minute(acres)
    # # print_acres(acres)
    # total = count_total(acres)
    # result = total['#'] * total['|']
    # if i > 1000:
        # totals[i] = result
    # totals[result] += 1

# print(totals)
# for total, val in totals.items():
    # if val > 10:
        # print(total)

# prvy je 1000
asd = {0: 189504, 1: 192440, 2: 193890, 3: 192855, 4: 192444, 5: 188442, 6: 185255, 7: 184470, 8: 181582, 9: 180144, 10: 178476, 11: 179118, 12: 180468, 13: 185148, 14: 179439, 15: 182325, 16: 186120, 17: 189840, 18: 191080, 19: 192296, 20: 192997, 21: 189608, 22: 188421, 23: 185504, 24: 184548, 25: 184368, 26: 186147, 27: 189168}

num = 1000000000
print(asd[(num - 1001) % len(asd)])
