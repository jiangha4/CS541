import argparse
from helpers.population import *
from helpers.selection import *
from helpers.myheapq import *

def argument_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-p', '--population', type=int, action='store',
                        help='The initial population size')
    return parser.parse_args()


def main():
    pop, avg_fitness = generate_population(10)
    queue = MyHeapQueue()
    selection_percentage(pop, avg_fitness, queue)
    new_pop = []
    while queue.length > 1:
        parent_one, parent_two = queue.pop()
        seq_one, seq_two = crossover(parent_one, parent_two)
        child_one = individual(sequence=seq_one)
        child_two = individual(sequence=seq_two)
        mutations(child_one, child_two)
        new_pop.append(child_one)
        new_pop.append(child_two)


def check_goal(population):
    for ind in population:
        if ind.fitness == 0:
            return ind
    return None


if __name__ == '__main__':
    main()
