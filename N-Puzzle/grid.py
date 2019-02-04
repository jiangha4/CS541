import copy

class Grid(object):
    leftEdge = [0, 3, 6]
    rightEdge = [2, 5, 8]

    def __init__(self, size, numlist):
        self.grid = numlist
        self.size = size
        self.length = len(self.grid)
        self.parity = self.parity()

    def parity(self):
        parity = 0
        for i in range(0, self.length):
            cur = self.grid[i]
            for j in range(i+1, self.length):
                if cur > self.grid[j]:
                    parity = parity + 1
        return parity

    def actions(self):
        blank_index = self.grid.index('b')
        successor = []
        if blank_index < 6:
            nextState = copy.deepcopy(self.grid)
            self.down(blank_index, nextState)
            successor.append(nextState)

        if blank_index > 3:
            nextState = copy.deepcopy(self.grid)
            self.up(blank_index, nextState)
            successor.append(nextState)

        if blank_index not in Grid.rightEdge:
            nextState = copy.deepcopy(self.grid)
            self.right(blank_index, nextState)
            successor.append(nextState)

        if blank_index not in Grid.leftEdge:
            nextState = copy.deepcopy(self.grid)
            self.left(blank_index, nextState)
            successor.append(nextState)

        return successor

    def left(self, index, state):
        newIndex = index - 1
        self._swap(index, newIndex, state)

    def up(self, index, state):
        newIndex = index - self.size
        self._swap(index, newIndex, state)

    def right(self, index, state):
        newIndex = index + 1
        self._swap(index, newIndex, state)

    def down(self, index, state):
        newIndex = index + self.size
        self._swap(index, newIndex, state)

    def _swap(self, x, y, layout):
        tmp = layout[x]
        layout[x] = layout[y]
        layout[y] = tmp

    def __repr__(self):
        rep = ''
        counter = 0
        for i in range(0, self.length):
            counter = counter + 1
            rep = rep + str(self.grid[i])
            if counter%self.size == 0:
                rep = rep + '\n'
        return rep


if __name__ == '__main__':
    testList = ['1', '2', '3', '4', '5', '6', '7', '8', 'b']
    a = Grid(3, testList)
    print(a)

