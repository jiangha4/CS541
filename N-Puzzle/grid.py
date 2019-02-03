class Square(object):
    def __init__(self, id):
        self.id = id

    def __gt__(self, other):
        if int(self.id) == -1:
            return False
        if int(other.id) == -1:
            return False
        return int(self.id) > int(other.id)

    def __repr__(self):
        if self.id == '-1':
            return '[b]'
        return '[' + self.id + ']'

class Grid(object):
    def __init__(self, size, numlist):
        self.numList = numlist
        self.grid = self.create_grid()
        self.size = size
        self.length = len(self.grid)
        self.parity = self.parity()

    def create_grid(self):
        grid = list()
        for elem in self.numList:
            if elem == 'b':
                grid.append(Square('-1'))
            else:
                grid.append(Square(elem))
        return grid

    def parity(self):
        parity = 0
        for i in range(0, self.length):
            cur = self.grid[i]
            for j in range(i+1, self.length):
                if cur > self.grid[j]:
                    parity = parity + 1
        return parity

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

