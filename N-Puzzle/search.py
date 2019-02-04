from grid import Grid
from node import Node, MyHeapQueue
from helper import *
import argparse

goal_grid = Grid(3, ['1', '2', '3', '4', '5', '6', '7', '8', 'b'])


def generate_successors(node, queue):
    for state in node.action:
        newGrid = Grid(3, state)
        heur = misplaced_square_heuristic(newGrid, goal_grid)
        depth = node.depth + 1
        newNode = Node(newGrid, node, heur, depth)
        if check_goal(newGrid, goal_grid):
            print('Found solution')
            return newNode
        queue.push(newNode)
    return None


def best_first_search(start_node):
    queue = MyHeapQueue()
    queue.push(start_node)
    while not queue.isEmpty():
        curr = queue.pop()
        curr.visited()
        goal = generate_successors(curr, queue)
        if goal:
            return goal
        queue.heapify()
    return None


def argument_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--init', type=str, action='store',
                        help='The initial puzzle state')
    return parser.parse_args()


def main():
    arg = argument_parser()
    starter_grid = Grid(3, list(arg.init))
    if check_parity(starter_grid, goal_grid):
        heur = misplaced_square_heuristic(starter_grid, goal_grid)
        #heur = manhattan_distance_heuristic(starter_grid, goal_grid)
        #heur = euclidean_distance_heuristic(starter_grid, goal_grid)
        starter_node = Node(starter_grid, None, heur, 0)
        goal = best_first_search(starter_node)
        backtrack(goal)
    else:
        print("Input parity is different from goal parity. Cannot solve.")


if __name__ == '__main__':
    main()


