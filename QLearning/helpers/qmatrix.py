import itertools
import copy

# generates all possible combinations of states
def generate_states():
    possible_states = list(itertools.product([0, 1, 2], repeat=5))
    return possible_states

# generate column
def init_column(states):
    qmatrix = {}
    for state in states:
        qmatrix[state] = 0
    return qmatrix

# generate qmatrix
def init_qmatrix(col):
    qmatrix = []
    for i in range(0, 5):
        qmatrix.append(copy.deepcopy(col))
    return qmatrix

def generate_qmatrix():
    possible_states = generate_states()
    column = init_column(possible_states)
    qmatrix = init_qmatrix(column)
    return qmatrix