from pprint import pprint
data = []
nodes = set()
counts = {}
with open('7.txt') as f:
# with open('7-example.txt') as f:
    for line in f.readlines():
        splitted = line.split(' ')
        first = splitted[1]
        second = splitted[7]
        nodes.add(first)
        nodes.add(second)
        if first not in counts:
            counts[first] = [0, []]
        if second not in counts:
            counts[second] = [0, []]
        counts[second][0] += 1
        counts[first][1].append(second)

pprint(counts)
from sortedcontainers import SortedSet
candidates = SortedSet()
for node, params in counts.items():
    if params[0] == 0:
        candidates.add(node)

result = ''
while candidates:
    # find first candidate and remove
    for candidate in candidates:
        if counts[candidate][0] == 0:
            break
    candidates.remove(candidate)
    # print('selecting', candidate)
    count, neighbors = counts[candidate]
    for n in neighbors:
        counts[n][0] -= 1
        candidates.add(n)

    del counts[candidate]

    result += candidate

    # print('next to consider', candidates)
    # print('counts', counts)
    # asd
    # for c
    # print(candidate)

print(result)
