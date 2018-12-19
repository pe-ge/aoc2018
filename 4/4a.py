from datetime import datetime

data = []
with open('4.txt') as f:
# with open('4-example.txt') as f:
    for line in f.readlines():
        splitted = line.split('] ')
        date = datetime.strptime(splitted[0], '[%Y-%m-%d %H:%M')
        event = splitted[1][:-1]

        data.append((date, event))

data = list(sorted(data, key=lambda d: d[0]))

records = {}
guard_id = None
falls_asleep = None
for date, event in data:
    if event[0] == 'G':  # begins shift
        guard_id = int(event.split(' ')[1][1:])
        if guard_id not in records:
            records[guard_id] = [0] * 60
    elif event[0] == 'f':  # falls asleep
        falls_asleep = date.minute
    elif event[0] == 'w':  # wakes up
        wakes_up = date.minute
        for i in range(falls_asleep, wakes_up):
            records[guard_id][i] += 1

# find most sleepy guard
most_asleep_minutes = 0
most_asleep_idx = None
for guard_idx, minutes in records.items():
    total_minutes = sum(minutes)
    if total_minutes > most_asleep_minutes:
        most_asleep_minutes = total_minutes
        most_asleep_idx = guard_idx

# find most slept minute
max_minute = 0
max_minute_idx = None
for minute_idx, minute in enumerate(records[most_asleep_idx]):
    if minute > max_minute:
        max_minute = minute
        max_minute_idx = minute_idx

print(most_asleep_idx * max_minute_idx)
