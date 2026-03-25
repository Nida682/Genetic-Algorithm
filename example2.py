import random

# Each number represents a time slot (1–5)
def fitness(schedule):
    # Penalize duplicate time slots (conflicts)
    return len(set(schedule))

# Initial schedules (5 classes)
population = [[random.randint(1, 5) for _ in range(5)] for _ in range(5)]

for generation in range(5):
    population = sorted(population, key=fitness, reverse=True)
    print("Generation:", generation, "Best Schedule:", population[0])

    # Crossover
    new_population = population[:2]
    while len(new_population) < 5:
        p1, p2 = random.sample(population[:3], 2)
        point = random.randint(1, 3)
        child = p1[:point] + p2[point:]
        new_population.append(child)

    # Mutation
    population = []
    for sched in new_population:
        idx = random.randint(0, 4)
        sched[idx] = random.randint(1, 5)
        population.append(sched)
