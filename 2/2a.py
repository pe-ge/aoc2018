data = []
with open('2.txt') as f:
    for line in f.readlines():
        data.append(line[:-1])

twos = 0
threes = 0
for string in data:
    freq_table = {}
    for char in string:
        if char not in freq_table:
            freq_table[char] = 0
        freq_table[char] += 1

    two_found = False
    three_found = False
    for (k, v) in freq_table.items():
        if v == 2 and not two_found:
            twos += 1
            two_found = True
        elif v == 3 and not three_found:
            threes += 1
            three_found = True

print(twos * threes)
