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
    parser.add_argument('-b', '--best', action='store_true',
                        help='Use queue based selection')
    return parser.parse_args()

# roulette based selection
def reproduce(pop, popNum):
    new_pop = []
    selection_percentage(pop)
    best = get_best_individual(pop)
    for i in range(0, popNum):
        parent_one, parent_two = fitness_selection(pop)
        seq_one, seq_two = crossover(parent_one, parent_two)
        child_one = individual(sequence=seq_one)
        child_two = individual(sequence=seq_two)
        mutations(child_one, child_two)
        new_pop.append(child_one)
        new_pop.append(child_two)
    return new_pop, best

# Queued based selection
def queue_reproduce(pop):
    queue = MyHeapQueue()
    selection_percentage(pop, queue)
    best = queue.peek()
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
    return new_pop, best


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
    plt.title('Generation vs fitness for initial population size of: {}'.format(genNum))
    plt.show()

def main(args):
    if args.population:
        gen_num = args.population
    else:
        gen_num = 1000
    population, total_fitness = generate_population(gen_num)
    fitness_per_generation = [total_fitness/len(population)]
    best_fitness_per_generation = []
    goal = None
    i = 0
    while not goal:
        print("General: {}".format(i))
        if not args.best:
            population, best_fitness = reproduce(population, gen_num)
        else:
            population, best_fitness = queue_reproduce(population)
        goal = check_goal(population)
        i += 1

        if args.graph:
            fitness_per_generation.append(get_max_fitness(population)/len(population))
            best_fitness_per_generation.append(best_fitness.fitness)

        print(best_fitness)
        if i > 1000:
            break
    print("Goal state: {}".format(goal))
    print("Generations taken: {}".format(i))
    if args.graph:
        make_graph(i, fitness_per_generation, best_fitness_per_generation, gen_num)


if __name__ == '__main__':
    args = argument_parser()
    main(args)
