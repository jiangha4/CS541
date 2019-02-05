import heapq

class MyHeapQueue(object):
    def __init__(self, key=lambda x:x):
        self.key = key
        self._data = []
        self._visited = []

    def push(self, node):
        if node not in self._visited:
            heapq.heappush(self._data, (node.path_cost, node))
            self._visited.append(node)
            heapq.heapify(self._data)

    def pop(self):
        return heapq.heappop(self._data)[1]

    def isEmpty(self):
        if len(self._data) == 0:
            return True
        return False
