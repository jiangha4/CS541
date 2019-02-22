from random import shuffle

class individual(object):
    def __init__(self, sequence=None):
        if sequence == None:
            self.sequence = self.generate()
        else:
            self.sequence = sequence
        self.fitness = self.fitness()
        self.fitness_percentage = None

    def generate(self):
        indiviual = [x for x in range(0,8)]
        shuffle(indiviual)
        return indiviual

    def fitness(self):
        count = abs(len(self.sequence) - len(set(self.sequence)))

        for i in range(0, 7):
            for j in range(0, 7):
                if i != j:
                    x = abs(i-j)
                    y = abs(self.sequence[i] - self.sequence[j])
                    if x==y:
                        count += 1
        return count

    def set_fitness_percentage(self, percentage):
        self.fitness_percentage = percentage

    def __le__(self, other):
        return self.fitness_percentage <= other.fitness_percentage

    def __lt__(self, other):
        return self.fitness_percentage < other.fitness_percentage

    def __repr__(self):
        return str(self.sequence)


def generate_population(populationSize):
    pop = []
    total_fitness = 0
    for i in range(1, populationSize):
        ind = individual()
        total_fitness += ind.fitness
        pop.append(ind)
    return pop, total_fitness