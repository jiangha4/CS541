import heapq

class Node(object):
    def __init__(self, state, parent, path_cost, depth):
        self.state = state
        self.parent = parent
        self.action = state.actions()
        self.path_cost = path_cost
        self.visit = False
        self.depth = depth

    def visited(self):
        self.visit = True

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __repr__(self):
        return str(self.state) + 'Heurisitic Value:' + str(self.path_cost)

class MyHeapQueue(object):
    def __init__(self, key=lambda x:x):
        self.key = key
        self._data = []

    def push(self, node):
        heapq.heappush(self._data, (node.path_cost, node))

    def pop(self):
        return heapq.heappop(self._data)[1]

    def heapify(self):
        heapq.heapify(self._data)

    def isEmpty(self):
        if len(self._data) == 0:
            return True
        return False
