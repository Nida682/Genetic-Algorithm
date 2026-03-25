import random

# Suppose we have 5 features (1 = selected, 0 = not selected)
def fitness(solution):
    # Simulated accuracy (more selected features ≠ always better)
    return sum(solution) - 0.5 * solution.count(0)

# Initial population (random feature subsets)
population = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]

for generation in range(5):
    population = sorted(population, key=fitness, reverse=True)
    print("Generation:", generation, "Best:", population[0], "Score:", fitness(population[0]))

    # Crossover
    new_population = population[:2]
    while len(new_population) < 5:
        p1, p2 = random.sample(population[:3], 2)
        crossover_point = random.randint(1, 3)
        child = p1[:crossover_point] + p2[crossover_point:]
        new_population.append(child)

    # Mutation
    population = []
    for individual in new_population:
        idx = random.randint(0, 4)
        individual[idx] = 1 - individual[idx]
        population.append(individual)
