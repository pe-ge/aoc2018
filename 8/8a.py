data = []
with open('8.txt') as f:
# with open('8-example.txt') as f:
    for line in f.readlines():
        data = [int(x) for x in line.split(' ')]


class Node:

    curr_idx = 0
    sum_meta = 0

    def __init__(self, parent):
        self.parent = parent
        self.children = []
        self.meta = []

    def parse(self):
        num_child = data[Node.curr_idx]
        num_meta = data[Node.curr_idx+1]
        Node.curr_idx += 2

        for child_idx in range(num_child):
            children = Node(self)
            children.parse()
            self.children.append(children)

        for meta_idx in range(num_meta):
            self.meta.append(data[Node.curr_idx])
            Node.sum_meta += data[Node.curr_idx]
            Node.curr_idx += 1


root = Node(None)
root.parse()
print(root.sum_meta)
