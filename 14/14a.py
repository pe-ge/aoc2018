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
                return self.value == other.value and self.left.value == other.left.value and self.right.value == other.right.value
            return False

    def __init__(self, num_recipes):
        self.last = None
        self.first = None
        self.num_recipes = num_recipes
        self.length = 0

        self.current1 = None
        self.current2 = None

    def __len__(self):
        return self.length

    def insert(self, value):
        new_node = CLL.Node(value)
        if self.current1 is None:
            self.current1 = new_node
            self.current1.left = self.current1
            self.current1.right = self.current1

            self.last = self.current1
            self.first = self.current1
        else:
            new_node.right = self.last.right
            new_node.right.left = new_node
            new_node.left = self.last
            self.last.right = new_node
            self.last = new_node

            if self.num_recipes > 0:
                self.num_recipes -= 1
                self.first = self.first.right

            if self.current2 is None:
                self.current2 = new_node

        self.length += 1

    def insert_value(self):
        value = self.current1.value + self.current2.value
        digits = list(map(int, str(value)))
        for d in digits:
            self.insert(d)

        self.move_first(self.current1.value + 1)
        self.move_second(self.current2.value + 1)

    def move_first(self, count=1):
        for _ in range(count):
            self.current1 = self.current1.right

    def move_second(self, count=1):
        for _ in range(count):
            self.current2 = self.current2.right

    def get_score(self, count):
        score = []
        for i in range(count):
            score.append(str(self.first.value))
            self.first = self.first.right

        return ''.join(score)

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


num_recipes = 556061
recipes = CLL(num_recipes)
recipes.insert(3)
recipes.insert(7)

while len(recipes) < num_recipes + 10:
    recipes.insert_value()
print(recipes)
print(recipes.first)
print(recipes.get_score(10))
