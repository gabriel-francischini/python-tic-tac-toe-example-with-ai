from main import play_game
import random
from random import randint

def randpos():
    return (randint(0, 2), randint(0,2))

genome_size = 100

class It():

    def __init__(self):
        self.genome = []
        self.score = 0
        for i in range(genome_size):
            self.genome.append(randpos())

    def play(self, board):
        # Try positions based on genome
        for x, y in self.genome:
            if board[x][y] == ' ':
                return (x, y)

        # If anything else doesn't work,
        # try random moves
        while True:
            x, y = randpos()
            if board[x][y] == ' ':
                return (x, y)
        

pop_size = 30
n_enemies = 5
n_games = 5
mutation_chance = 0.05
generations = 100
population = [It() for i in range(pop_size)]


for generation in range(0, generations):
    print("Simulation generation " + str(generation) + "...")
    
    for one in population:
        enemies = random.sample(population, n_enemies)

        for enemy in enemies:
            one_s, enemy_s = play_game(one.play, enemy.play, N=n_games)
            one.score += one_s
            enemy.score += enemy_s

    population.sort(key=lambda x: x.score, reverse=True)
    strongest = population[0:5]

    new_population = []
    for i in range(pop_size):
        father = random.choice(strongest)
        mother = random.choice(strongest)

        crossover_point = random.randint(0, genome_size-1)

        child = It()
        child.genome = father.genome[0:crossover_point] + mother.genome[crossover_point:100]

        for index, value in enumerate(child.genome):
            # Should we mutate?
            if random.random() < mutation_chance:
                child.genome[index] = randpos()

        new_population.append(child)

    old_population = population
    population = new_population

old_population.sort(key=lambda x: x.score, reverse=True)
a, b = old_population[0:2]
play_game(a.play, b.play, N=1, should_print_board=True)
