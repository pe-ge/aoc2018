# cyclic linked list
class CLL:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return str(self.value)

        def __eq__(self, other):
            if isinstance(other, CLL.Node):
                return self.value == other.value
            return False

    def __init__(self):
        self.current = None
        self.length = 0

    def __len__(self):
        return self.length

    def insert(self, value):
        new_node = CLL.Node(value)
        if self.current is None:
            self.current = new_node
            self.current.left = self.current
            self.current.right = self.current
        else:
            new_node.right = self.current.right
            new_node.right.left = new_node
            new_node.left = self.current
            self.current.right = new_node

            self.current = new_node

        self.length += 1

    def remove(self):
        self.current.left.right = self.current.right
        self.current.right.left = self.current.left
        self.current = self.current.right

        self.length -= 1

    def move_left(self, count=1):
        for _ in range(count):
            self.current = self.current.left

    def move_right(self, count=1):
        for _ in range(count):
            self.current = self.current.right

    def __str__(self):
        tmp = self.current
        last = tmp.left
        result = []
        while last != tmp:
            result.append(str(tmp))
            tmp = tmp.right

        result.append(str(last))

        return ','.join(result)


data = open('9.txt').read().split()
# data = open('9-example4.txt').read().split()
players = int(data[0])
last_marble = int(data[6]) * 100

scores = {i: 0 for i in range(1, players+1)}

marbles = CLL()
marbles.insert(0)

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
        marbles.move_left(7)
        # append to score
        scores[curr_player] += marbles.current.value
        # remove marble at this index
        marbles.remove()
    else:
        marbles.move_right()
        marbles.insert(curr_marble)

    # print(marbles)
    curr_player = curr_player % players + 1

# print(scores)
max_score = 0
for k, v in scores.items():
    max_score = max(max_score, v)
print(max_score)
