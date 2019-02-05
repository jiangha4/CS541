import argparse
from search import *


def argument_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--init', type=str, action='store',
                        help='The initial puzzle state')
    parser.add_argument('-m', '--miss', action='store_true',
                        help='Use missing tile heuristic')
    parser.add_argument('-d', '--man', action='store_true',
                        help='Use manhattan distance heuristic')
    parser.add_argument('-e', '--eucl', action='store_true',
                        help='Use euclidean distance heuristic')
    parser.add_argument('-c', '--cycles', type=int, action='store', required=True,
                        help='Number of cycles')
    return parser.parse_args()

def search_function(starter_grid, heur_function):
    print("Best first Search")
    goal = best_first_search(starter_grid, heur_function)
    if goal:
        best_first_steps = backtrack(goal)

    goal = a_star_search(starter_grid, heur_function)
    print("A* search")
    if goal:
        a_star_steps = backtrack(goal)
    return best_first_steps, a_star_steps

def main():
    arg = argument_parser()
    starter_grid = Grid(3, list(arg.init))
    if check_parity(starter_grid, goal_grid):
        goal_average_best_first = []
        goal_average_a_star = []
        for i in range(0, arg.cycles):
            print("Trial {}".format(i))
            if arg.miss:
                best_first_steps, a_star_steps = search_function(starter_grid, misplaced_square_heuristic)
                goal_average_best_first.append(best_first_steps)
                goal_average_a_star.append(a_star_steps)
            elif arg.man:
                best_first_steps, a_star_steps = search_function(starter_grid, manhattan_distance_heuristic)
                goal_average_best_first.append(best_first_steps)
                goal_average_a_star.append(a_star_steps)
            elif arg.eucl:
                best_first_steps, a_star_steps = search_function(starter_grid, euclidean_distance_heuristic)
                goal_average_best_first.append(best_first_steps)
                goal_average_a_star.append(a_star_steps)
        print("Average steps for best first search: {}".format(sum(goal_average_best_first)/arg.cycles))
        print("Average steps for a star search: {}".format(sum(goal_average_a_star)/arg.cycles))

    else:
        print("Input parity is different from goal parity. Cannot solve.")


if __name__ == '__main__':
    main()
