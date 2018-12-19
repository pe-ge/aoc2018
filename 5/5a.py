polymer = []
# with open('5-example.txt') as f:
with open('5.txt') as f:
    data = f.readlines()[0][:-1]
    for d in data:
        polymer.append(d)

idx = 0
while idx < len(polymer) - 1:
    first = polymer[idx]
    second = polymer[idx+1]
    if abs(ord(first) - ord(second)) == 32:
        del polymer[idx]
        del polymer[idx]
        idx -= 1
    else:
        idx += 1

print(len(polymer))
