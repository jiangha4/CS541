import heapq

class MyHeapQueue(object):
    def __init__(self, key=lambda x:x):
        self.key = key
        self._data = []
        self._visited = set()

    def push(self, node):
        hash_rep = ''.join(node.state.grid)
        if hash_rep not in self._visited:
            heapq.heappush(self._data, (node.path_cost, node))
            self._visited.add(hash_rep)

    def pop(self):
        return heapq.heappop(self._data)[1]

    def isEmpty(self):
        if len(self._data) == 0:
            return True
        return False

if __name__ == '__main__':
    pass

