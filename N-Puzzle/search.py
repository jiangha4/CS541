from grid import Grid
import argparse

class Node(object):
    def __init__(self):
        self.state = None
        self.parent = None
        self.action = None
        self.path_cost = None


class SearchTree(object):
    def __init__(self):
        pass


def best_first_search(start_state):
    print(start_state.parity)

def a_star_search():
    pass


def argument_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--init', type=str, action='store',
                        help='The initial puzzle state')
    return parser.parse_args()


if __name__ == '__main__':
    arg = argument_parser()
    start_state = Grid(3, list(arg.init))
    print(start_state)
    best_first_search(start_state)

