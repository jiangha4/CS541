import argparse
from helpers.population import *
from helpers.selection import *
from helpers.myheapq import *


def argument_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-p', '--population', type=int, action='store',
                        help='The initial population size')
    parser.add_argument('-g', '--graph', action='store_true',
                        help='Show graphs. Must have matplotlib package installed')
    return parser.parse_args()


def reproduce(pop, totalFitness):
    queue = MyHeapQueue()
    selection_percentage(pop, totalFitness, queue)
    new_pop = []
    total_fitness = 0
    while queue.length > 1:
        parent_one, parent_two = queue.pop()
        seq_one, seq_two = crossover(parent_one, parent_two)
        child_one = individual(sequence=seq_one)
        child_two = individual(sequence=seq_two)
        mutations(child_one, child_two)
        new_pop.append(child_one)
        new_pop.append(child_two)
        total_fitness += child_one.fitness + child_two.fitness
    return new_pop, total_fitness


def check_goal(population):
    for ind in population:
        if ind.fitness == 0:
            return ind
    return None


def make_graph(generations, avg_fitness):
    import matplotlib.pyplot as plt
    xaxis = [x for x in range(0, generations)]
    plt.plot(xaxis, avg_fitness)
    plt.ylabel('Average fitness')
    plt.xlabel('Generation')
    plt.show()

def main(args):
    pop, total_fitness = generate_population(10)
    generations = 1000
    fitness_per_generation = [total_fitness/len(pop)]
    for i in range(0, generations):
        population, total_fitness = reproduce(pop, total_fitness)
        if args.graph:
            fitness_per_generation.append(total_fitness/len(population))
        #goal = check_goal(population)
        #if goal:
        #    print(goal, i)
        #    return goal

    if args.graph:
        make_graph(generations, fitness_per_generation)

if __name__ == '__main__':
    args = argument_parser()
    main(args)
