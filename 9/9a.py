
data = open('9.txt').read().split()
# data = open('9-example3.txt').read().split()
players = int(data[0])
last_marble = int(data[6])

scores = {i: 0 for i in range(1, players+1)}
marbles = list()

marbles.append(0)
curr_player = 1
curr_marble = 1
curr_idx = 1
for curr_marble in range(1, last_marble+1):
    if curr_marble % 1000 == 0:
        print(curr_marble / last_marble)
    if curr_marble % 23 == 0:
        # append to score
        scores[curr_player] += curr_marble
        # shift current index 7 counterclockwise
        # print(curr_idx)
        # print(len(marbles))
        curr_idx = (curr_idx - 7) % (len(marbles))
        # curr_idx = max(curr_idx, 1)
        # append to score
        # print(curr_idx)
        scores[curr_player] += marbles[curr_idx]
        # remove marble at this index
        # print('mazem')
        del marbles[curr_idx]
        # print(marbles)
        # if curr_marble == 46:
        # asd
    else:
        curr_idx = (curr_idx + 2) % (len(marbles)+1)
        curr_idx = max(curr_idx, 1)
        # print('insertujem')
        marbles.insert(curr_idx, curr_marble)

    # print(marbles)
    curr_player = curr_player % players + 1

print(scores)
max_score = 0
for k, v in scores.items():
    max_score = max(max_score, v)
print(max_score)
