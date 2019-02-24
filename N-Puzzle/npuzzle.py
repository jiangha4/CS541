import argparse
import time
from helpers.search import *


def argument_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t', '--three', type=str, action='store',
                        help='The initial puzzle state')
    parser.add_argument('-m', '--miss', action='store_true',
                        help='Use missing tile heuristic')
    parser.add_argument('-d', '--man', action='store_true',
                        help='Use manhattan distance heuristic')
    parser.add_argument('-e', '--eucl', action='store_true',
                        help='Use euclidean distance heuristic')
    parser.add_argument('-c', '--cycles', type=int, action='store', required=True,
                        help='Number of cycles')
    parser.add_argument('-f', '--four', type=str, action='store',
                        help="Solve 15-Puzzle")
    return parser.parse_args()


def search_function(starter_grid, heur_function, goal_grid):
    print("Best first Search")
    start_time = time.time()
    goal = best_first_search(starter_grid, heur_function, goal_grid)
    best_first_duration = time.time() - start_time
    print("Search duration: {}".format(best_first_duration))
    if goal:
        best_first_steps = backtrack(goal)

    print("A* search")
    start_time = time.time()
    goal = a_star_search(starter_grid, heur_function, goal_grid)
    a_star_duration = time.time() - start_time
    print("Search duration: {}".format(a_star_duration))
    if goal:
        a_star_steps = backtrack(goal)
    return best_first_steps, a_star_steps


def main():
    arg = argument_parser()
    if arg.three:
        starter_grid = three_Grid((arg.three).split(','))
        goal_grid = three_Grid(['1', '2', '3', '4', '5', '6', '7', '8', 'b'])
        print(starter_grid)
    if arg.four:
        starter_grid= four_Grid((arg.four).split(','))
        goal_grid = four_Grid('1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,b'.split(','))
    if check_parity(starter_grid, goal_grid):
        goal_average_best_first = []
        goal_average_a_star = []
        for i in range(0, arg.cycles):
            print("Trial {}".format(i))
            if not arg.four:
                if arg.miss:
                    best_first_steps, a_star_steps = search_function(starter_grid, misplaced_square_heuristic, goal_grid)
                    goal_average_best_first.append(best_first_steps)
                    goal_average_a_star.append(a_star_steps)
                elif arg.man:
                    best_first_steps, a_star_steps = search_function(starter_grid, manhattan_distance_heuristic, goal_grid)
                    goal_average_best_first.append(best_first_steps)
                    goal_average_a_star.append(a_star_steps)
                elif arg.eucl:
                    best_first_steps, a_star_steps = search_function(starter_grid, euclidean_distance_heuristic, goal_grid)
                    goal_average_best_first.append(best_first_steps)
                    goal_average_a_star.append(a_star_steps)
            else:
                if arg.miss:
                    best_first_steps, a_star_steps = search_function(starter_grid, misplaced_square_heuristic, goal_grid)
                    goal_average_best_first.append(best_first_steps)
                    goal_average_a_star.append(a_star_steps)
                elif arg.man:
                    best_first_steps, a_star_steps = search_function(starter_grid, manhattan_distance_heuristic, goal_grid)
                    goal_average_best_first.append(best_first_steps)
                    goal_average_a_star.append(a_star_steps)
                elif arg.eucl:
                    best_first_steps, a_star_steps = search_function(starter_grid, euclidean_distance_heuristic, goal_grid)
                    goal_average_best_first.append(best_first_steps)
                    goal_average_a_star.append(a_star_steps)
        print("Average steps for best first search: {}".format(sum(goal_average_best_first)/arg.cycles))
        print("Average steps for a star search: {}".format(sum(goal_average_a_star)/arg.cycles))

    else:
        print("Input parity is different from goal parity. Cannot solve.")


if __name__ == '__main__':
    main()