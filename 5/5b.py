polymer = []
# with open('5-example.txt') as f:
with open('5.txt') as f:
    data = f.readlines()[0][:-1]
    for d in data:
        polymer.append(d)

def react(polymer):
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
    return polymer


chars = [chr(x) for x in range(97, 123)]
min_len = 999999
for ch in chars:
    p = ''.join(polymer)
    p = p.replace(ch, '')
    p = p.replace(ch.upper(), '')
    p = list(p)
    min_len = min(min_len, len(react(p)))

print(min_len)
