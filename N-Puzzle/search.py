from grid import Grid
from node import Node, MyHeapQueue
from helper import *
import argparse

goal_grid = Grid(3, ['1', '2', '3', '4', '5', '6', '7', '8', 'b'])


def best_first_search(start_node):
    queue = MyHeapQueue()
    queue.push(start_node)
    while not queue.isEmpty():
        curr = queue.pop()
        print(curr.state)


def argument_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--init', type=str, action='store',
                        help='The initial puzzle state')
    return parser.parse_args()


def main():
    arg = argument_parser()
    starter_grid = Grid(3, list(arg.init))
    if check_parity(starter_grid, goal_grid):
        #heur = misplaced_square_heuristic(starter_grid, goal_grid)
        #heur = manhattan_distance_heuristic(starter_grid, goal_grid)
        heur = euclidean_distance_heuristic(starter_grid, goal_grid)
        print(heur)
        starter_node = Node(starter_grid, None, None, heur)
        best_first_search(starter_node)
    else:
        print("Input parity is different from goal parity. Cannot solve.")


if __name__ == '__main__':
    main()


