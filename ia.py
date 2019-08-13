from main import play_game
import random
from random import randint
from neural import NeuralNetwork

def randgene():
    return random.uniform(-1,1)

# 'nn' stands for NeuralNetwork
nn_inputs = 9
nn_hidden = 2
nn_hidden_size = 3
nn_output = 9 # Each output is interpreted as probability of best move

genome_size = (nn_inputs * nn_inputs # Weights on 1st layer
               + nn_hidden_size * nn_inputs # Weights on 1st hidden
               + (nn_hidden - 1) * nn_hidden_size * nn_hidden_size # Remaining hidden
               + nn_output * nn_hidden_size # Output layer
)
pop_size = 30
n_enemies = 5
n_games = 5
mutation_chance = 0.05
generations = 30




class It():

    def __init__(self):
        self.genome = []
        self.score = 0
        self.symbol = 'O'
        self.another = 'X'
        for i in range(genome_size):
            self.genome.append(randgene())

    def play(self, board):
        nn = NeuralNetwork(n_inputs = nn_inputs,
                           n_hidden = nn_hidden,
                           size_hidden = nn_hidden_size,
                           n_output = nn_output,
                           weights = self.genome)

        flattened_board = board[0] + board[1] + board[2]
        floats = [{self.another: 0.0,
                   ' ': 0.5,
                   self.symbol: 1.0}[char]
                  for char in flattened_board]
        possibilities = nn.evaluate(floats)

        coords = {}
        for i in range(0,3):
            for j in range(0,3):
                coords[(i, j)] = possibilities[i * 3 + j]

        best_moves = sorted(list(coords.items()), key=lambda x: x[-1])
        # print(best_moves)
        for coord, score in best_moves:
            x, y = coord
            if board[x][y] == ' ':
                return (x, y)

        print(possibilities)

        def randpos():
            return (randint(0, 2), randint(0,2))

        while True:
            x, y = randpos()
            if board[x][y] == ' ':
                return (x, y)




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
                child.genome[index] = randgene()

        new_population.append(child)

    old_population = population
    population = new_population

old_population.sort(key=lambda x: x.score, reverse=True)
a, b = old_population[0:2]
play_game(a.play, b.play, N=1, should_print_board=True)
