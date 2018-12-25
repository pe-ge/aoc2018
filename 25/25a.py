from pprint import pprint

data = open('25.txt').read().split('\n')
data = data[:-1]
data = [tuple(int(val) for val in line.split(',')) for line in data]


cons = [[point] for point in data]

def manhattan(a, b):
    return sum([abs(a[k] - b[k]) for k in range(len(a))])


end = False
while not end:
    end = True
    stop = False
    for c1_idx in range(len(cons)-1):
        for c2_idx in range(c1_idx+1, len(cons)):
            c1 = cons[c1_idx]
            c2 = cons[c2_idx]
            for p1 in c1:
                for p2 in c2:

                    distance = manhattan(p1, p2)
                    if distance <= 3:
                        c1.append(p2)
                        c2.remove(p2)
                        if len(c2) == 0:
                            cons.remove(c2)
                        stop = True
                        end = False
                    if stop:
                        break
                if stop:
                    break
            if stop:
                break
        if stop:
            break

print(len(cons))
