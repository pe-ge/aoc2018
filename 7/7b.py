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
free_tasks = SortedSet()
for node, params in counts.items():
    if params[0] == 0:
        free_tasks.add(node)

total_time = 0
workers = {i: [0, ''] for i in range(5)}
while counts:
    print('free tasks', free_tasks)

    # assign tasks
    for w in workers:
        if workers[w][0] == 0 and free_tasks:
            task = free_tasks.pop(0)
            workers[w][0] += ord(task) - 4
            workers[w][1] = task

            print('assiging', task, 'to worker', w)

    print('workers', workers)

    # finish task with least time
    min_time = 1000000
    for w in workers:
        if workers[w][0] > 0:
            min_time = min(workers[w][0], min_time)

    # move time
    print('waiting', min_time)
    total_time += min_time
    for w in workers:
        workers[w][0] -= min_time
        workers[w][0] = max(0, workers[w][0])
        # if task is completed
        if workers[w][1] and workers[w][0] == 0:
            # print(counts[workers[w][1]][1])
            completed_task = workers[w][1]
            # if already finished
            if completed_task == '':
                continue
            neigbors = counts[completed_task][1]
            # find new free tasks
            for n in neigbors:
                counts[n][0] -= 1
                if counts[n][0] == 0:
                    free_tasks.add(n)
            print('task', completed_task, 'is completed')
            del counts[completed_task]
            workers[w][1] = ''

print(total_time)
