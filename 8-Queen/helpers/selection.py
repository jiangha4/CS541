import random


def selection_percentage(population, avgFitness, queue):
    for ind in population:
        select_prob = ind.fitness/avgFitness
        ind.set_fitness_percentage(select_prob)
        queue.push(ind)


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

