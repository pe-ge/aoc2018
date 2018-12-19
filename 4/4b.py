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

# find most freq minute + guard
most_freq_minute = 0
most_freq_minute_idx = None
most_freq_minute_guard_idx = None
for guard_idx, minutes in records.items():
    for m_idx, m in enumerate(minutes):
        if m > most_freq_minute:
            most_freq_minute = m
            most_freq_minute_idx = m_idx
            most_freq_minute_guard_idx = guard_idx

print(most_freq_minute_idx * most_freq_minute_guard_idx)
