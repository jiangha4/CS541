class Node(object):
    def __init__(self, state, parent, path_cost, depth):
        self.state = state
        self.parent = parent
        self.action = state.actions()
        self.path_cost = path_cost
        self.depth = depth

    def __eq__(self, other):
        if other == None:
            return False
        return self.state == other.state

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __repr__(self):
        return str(self.state)

