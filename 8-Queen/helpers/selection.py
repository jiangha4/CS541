import random
from operator import attrgetter

def selection_percentage(population, queue=None):
    total = get_max_fitness(population)
    if not queue:
        for ind in population:
            select_prob = float(ind.fitness/total)
            ind.set_fitness_percentage(select_prob)
    else:
        for ind in population:
            select_prob = float(ind.fitness / total)
            ind.set_fitness_percentage(select_prob)
            queue.push(ind)

def get_best_individual(population):
    return min(population, key=attrgetter('fitness'))


def get_max_fitness(population):
    return sum([population[i].fitness for i in range(0, len(population))])


def fitness_selection(population):
    max = get_max_fitness(population)
    parent_one = None
    while not parent_one:
        rand = random.uniform(0, max)
        target = float(rand/max)
        potential = [ind for ind in population if ind.fitness_percentage <= target]
        try:
            parent_one = potential[random.randint(0, len(potential)-1)]
        except:
            parent_one = None

    parent_two = None
    while not parent_two:
        rand = random.uniform(0, max)
        target = float(rand/max)
        potential = [ind for ind in population if ind.fitness_percentage <= target]
        try:
            parent_two = potential[random.randint(0, len(potential)-1)]
            if parent_one == parent_two:
                print("parent clash")
                parent_two = None
        except:
            parent_two = None

    return parent_one, parent_two

def crossover(parentOne, parentTwo):
    crossover_index = random.randint(0, 7)
    seq_one = parentOne.sequence[0:crossover_index]
    seq_one.extend(parentTwo.sequence[crossover_index:])
    seq_two = parentTwo.sequence[0:crossover_index]
    seq_two.extend(parentOne.sequence[crossover_index:])
    return seq_one, seq_two

# 1% chance at mutation
def mutations(childOne, childTwo):
    mutation_chance_one = random.randint(0, 100)
    mutation_chance_two = random.randint(0, 100)
    if mutation_chance_one == 10:
        mutate(childOne)
    if mutation_chance_two == 10:
        mutate(childTwo)


def mutate(ind):
    mutation_index = random.randint(0, 7)
    mutation_value = random.randint(0, 7)
    ind.sequence[mutation_index] = mutation_value

