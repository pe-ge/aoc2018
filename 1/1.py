data = []
with open('1.txt') as f:
    for line in f.readlines():
        data.append(int(line))

print(sum(data))
# print(data)

twice = {0}
acc = 0
found = False
while not found:
    for d in data:
        acc += d
        if acc in twice:
            print(acc)
            found = True
            break
        else:
            twice.add(acc)
