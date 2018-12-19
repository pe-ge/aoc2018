data = []
with open('2.txt') as f:
    for line in f.readlines():
        data.append(line[:-1])

max_common = 0
winners = None
for i in range(len(data)):
    for j in range(i+1, len(data)):
        first_str = data[i]
        second_str = data[j]

        common = 0
        for k in range(len(first_str)):
            if first_str[k] == second_str[k]:
                common += 1

        if common > max_common:
            max_common = common
            winners = (first_str, second_str)

first_str, second_str = winners
result = ''
for k in range(len(first_str)):
    if first_str[k] == second_str[k]:
        result += first_str[k]

print(result)
