from collections import defaultdict

plants = []
rules = defaultdict(lambda: '.')
with open('12.txt') as f:
# with open('12-example.txt') as f:
    plants = f.readline().split()[2]
    first_pot = plants.find('#')

    f.readline()
    for line in f.readlines():
        splitted = line.split()
        rules[splitted[0]] = splitted[2]


def get_substr(string, start_idx, length=5):
    result = []
    if start_idx < 0:
        result.extend(-start_idx * ['.'])
        result.extend(string[0:length+start_idx])

    elif len(string) - start_idx < length:
        result.extend(string[start_idx:])
        result.extend((length - len(result)) * ['.'])

    else:
        result.extend(string[start_idx:start_idx+length])
    return ''.join(result)


shift = 0
modulo = 50
for i in range(50000000000):
    if i % modulo == 0:
        total = 0
        for idx, char in enumerate(plants):
            if char == '#':
                total += (idx + shift)
        modulo *= 10

        print(total)

    new_str = []
    for idx in range(-4, len(plants) + 4):
        subs = get_substr(plants, idx)
        new_str.append(rules[subs])

    if new_str[1] == '#':
        shift -= 1
    elif new_str[2] == '.':
        shift += 1

    # remove dots at beggining and end
    first_pot = None
    last_pot = None
    for idx, char in enumerate(new_str):
        if char == '#':
            if first_pot is None:
                first_pot = idx
            last_pot = idx

    plants = ''.join(new_str[first_pot:last_pot+1])
