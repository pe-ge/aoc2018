class LL:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return str(self.value)

        def __eq__(self, other):
            if isinstance(other, LL.Node):
                return self.value == other.value and self.left.value == other.left.value and self.right.value == other.right.value
            return False

    def __init__(self, score):
        self.last = None
        self.score = list(map(int, score))
        self.length = 0

        self.current1 = None
        self.current2 = None

    def __len__(self):
        return self.length

    def insert(self, value):
        new_node = LL.Node(value)
        if self.current1 is None:
            self.current1 = new_node
            self.current1.right = self.current1

            self.last = self.current1
        else:
            new_node.right = self.last.right
            new_node.right.left = new_node
            new_node.left = self.last
            self.last.right = new_node
            self.last = new_node

            if self.current2 is None:
                self.current2 = new_node
        self.length += 1

        # check for score
        if value == self.score[-1]:
            tmp = self.last.left
            idx = len(self.score) - 2
            while idx >= 0:
                if tmp is None or tmp.value != self.score[idx]:
                    return False
                idx -= 1
                tmp = tmp.left

            print(self.length - len(score))
            return True

        return False

    def insert_value(self):
        value = self.current1.value + self.current2.value
        digits = list(map(int, str(value)))
        for d in digits:
            if self.insert(d):
                return True

        self.move_first(self.current1.value + 1)
        self.move_second(self.current2.value + 1)

    def move_first(self, count=1):
        for _ in range(count):
            self.current1 = self.current1.right

    def move_second(self, count=1):
        for _ in range(count):
            self.current2 = self.current2.right

    def __str__(self):
        tmp = self.last.right
        last = tmp.left
        result = []
        while last != tmp:
            if tmp == self.current1:
                result.append('(%s)' % tmp)
            elif tmp == self.current2:
                result.append('[%s]' % tmp)
            else:
                result.append('%s' % tmp)
            tmp = tmp.right

        if last == self.current1:
            result.append('(%s)' % tmp)
        elif last == self.current2:
            result.append('[%s]' % tmp)
        else:
            result.append('%s' % tmp)

        return ','.join(result)


score = '51589'
score = '01245'
score = '92510'
score = '59414'
score = '556061'
recipes = LL(score)
recipes.insert(3)
recipes.insert(7)

while not recipes.insert_value():
    pass
# print(recipes)
