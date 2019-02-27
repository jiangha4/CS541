import heapq

class MyHeapQueue(object):
    def __init__(self, key=lambda x:x):
        self.key = key
        self._data = []
        self._visited = set()

    def push(self, ind, flag=False):
        hash_rep = ''.join(str(ind.sequence))
        if hash_rep in self._visited:
            pass
        else:
            heapq.heappush(self._data, (ind.fitness_percentage, ind))
            self._visited.add(hash_rep)


    def pop(self):
        return heapq.heappop(self._data)[1], heapq.heappop(self._data)[1]

    def isEmpty(self):
        if len(self._data) == 0:
            return True
        return False

    def peek(self):
        return self._data[0][1]

    @property
    def length(self):
        return len(self._data)

    def __repr__(self):
        buf = ''
        for item in self._data:
            buf += str(item) + '\n'
        return buf

if __name__ == '__main__':
    pass
