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
for i in range(10):
    # print(i)
    acres = one_minute(acres)
    # print_acres(acres)

total = count_total(acres)
print(total)
print(total['#'] * total['|'])
