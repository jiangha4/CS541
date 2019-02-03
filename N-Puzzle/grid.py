class Grid(object):
    leftEdge = [2, 5, 8]
    rightEdge = [0, 3, 6]
    topEdge = [0, 1, 2]
    botEdge = [6, 7, 8]

    actionEncoding = {'0': 'right', '1': 'left', '2': 'up', '3':'down'}

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
        buf = None
        blank_index = self.grid.index('b')
        if blank_index in Grid.leftEdge:
            pass
        elif blank_index in Grid.rightEdge:
            pass
        elif blank_index in Grid.topEdge:
            pass
        elif blank_index in Grid.botEdge:
            pass

    def left(self):
        pass

    def up(self):
        pass

    def right(self):
        pass

    def down(self):
        pass

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
    a = grid(3, testList)
    print(a)

