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
    best = (queue.peek()).fitness
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
        total_fitness = total_fitness + child_one.fitness + child_two.fitness
    return new_pop, total_fitness, best


def check_goal(population):
    for ind in population:
        if ind.fitness == 0:
            return ind
    return None


def make_graph(generations, avgFitness, bestFitness, genNum):
    import matplotlib.pyplot as plt

    f, axarr = plt.subplots(2, sharex=True)
    xaxis = [x for x in range(0, generations)]
    axarr[0].plot(xaxis, avgFitness[0:-1])
    axarr[1].plot(xaxis, bestFitness)
    axarr[0].set_ylabel('Average fitness')
    axarr[1].set_ylabel('Best fitness')
    plt.xlabel('Generation')
    plt.title('Generation vs average fitness for initial population size of: {}'.format(genNum))
    plt.show()


def main(args):
    if args.population:
        gen_num = args.population
    else:
        gen_num = 1000
    population, total_fitness = generate_population(gen_num)
    generations = 1000
    fitness_per_generation = [total_fitness/len(population)]
    best_fitness_per_generation = []
    for i in range(0, generations):
        population, total_fitness, best_fitness = reproduce(population, total_fitness)
        if args.graph:
            fitness_per_generation.append(total_fitness/len(population))
            best_fitness_per_generation.append(best_fitness)
        goal = check_goal(population)
        if goal:
            print(goal, i)

    if args.graph:
        make_graph(generations, fitness_per_generation, best_fitness_per_generation, gen_num)

if __name__ == '__main__':
    args = argument_parser()
    main(args)
