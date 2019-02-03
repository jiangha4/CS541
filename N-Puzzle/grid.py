class square(object):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '[' + self.id + ']'


class grid(object):
    def __init__(self, size,numList):
        self.numList = numList
        self.grid = self.createGrid()
        self.size = size

    def createGrid(self):
        grid = list()
        for elem in self.numList:
            grid.append(square(elem))
        return grid

    def __repr__(self):
        rep = ''
        counter = 0
        for i in range(0, len(self.grid)):
            counter = counter + 1
            rep = rep + str(self.grid[i])
            if counter%self.size == 0:
                rep = rep + '\n'
        return rep

if __name__ == '__main__':
    testList = ['1', '2', '3', '4', '5', '6', '7', '8', 'b']
    a = grid(3, testList)
    print(a)

