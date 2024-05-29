from random import randint, choices
import random


def generate_population(population_size, number_of_queens):
    """
        This function generates the population that we start with.
        Parameters
        - population_size (int): The Size of the population to generate.
        - number_queens (int): The number of queens in a particular individual. 
    """ 
    population = []
    for _ in range(population_size):
        individuals = []
        for _ in range(number_of_queens):
            individuals.append(randint(1, number_of_queens))
        population.append(individuals)
    return population

def calculate_fitness(individual):
    """
        This function calculates the fitness of a particular individual using the steps below:
        to calculate the fitness we need to subtract the number of pairs from the number of attacking pairs
        we go through the array, find the queens that are in the same row or diagonal then update our counter.
        Parameters
        - individual (list): A Solution list that we want to calculate the fitness for. 
    """
    number_of_pairs = 28
    attacking_pairs = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)): 
            if (individual[i] == individual[j]) or (abs((i) - (j)) == abs(individual[i] - individual[j])):
                attacking_pairs += 1
    return number_of_pairs - attacking_pairs

def selection(population, num_of_parents):
    """
        We select a set number of individuals based on their fitness score
        we go through the population array and calculate the fitness of each individual.
        Parameters
        - Population (All the individuals we want to select)
        - num_parents (The number of Parents we want to select for crossover ) 
    """
    fitness = [calculate_fitness(individual) for individual in population]
    sum_of_fitness = sum(fitness)
    selection_probablities = [(lambda x : x / sum_of_fitness)(score) for score in fitness]

    selected_parents = choices(population, weights=selection_probablities, k=num_of_parents)
    return selected_parents

def mutate(individual, mutation_rate= 0.1, number_of_queens=8):
    if(random.random() <= mutation_rate):
        individual[random.randint(0,7)] = randint(1, number_of_queens)  
    return individual

def crossover(parent1, parent2):
    """
        We have two parents then cut their genomes at an arbituary point to create a new individual
        Parameters
        - parent1 : (list of queen positions for the first parent)
        - parent2: (list of queen positions for the second parent) 
    """
    crossover_point = randint(1,len(parent1))
    return parent1[crossover_point: ] + parent2[:crossover_point]

def create_next_generation(current_population,mutation_rate):
    """ 
        We make use of each step in the genetic algorithm to create a new generation selection -> crossover -> mutation
        Parameters
        - current_population: (The population from the previous generation)
        - num_of_parents: (The number of parents to select)
        - mutation_rate: (The chances of  mutation should happening) 
    """
    new_population = []
    for _ in range(len(current_population)):
        parent1, parent2 = selection(current_population, 2)
        offspring = crossover(parent1, parent2)
        mutated_offspring = mutate(offspring, mutation_rate)
        new_population.append(mutated_offspring)
    return new_population


def check_for_termination(target_fitness, best_fitness, generation_count, max_generation):
    """
        This tells us when to stop finding new generations based on the generation count and  taregt fitness threshold
        Parameters
        - target_fitness: (The fitness value that indicates satisfaction with a particular solution)
        - best_fitness: (The best fitness for a particular generation)
        - generation_count: (The number of generations done so far)
        - max_generation: (The maximium number of generations allowed) 
    """
    if (generation_count >= max_generation):
        print("We have reached the max number of generations for this algorithm")
        return True
    if(best_fitness >= target_fitness):
        print("We have gotten the best solution for the algorithm")
        return True
    return False
def get_best_fitness(fitness):
    """ 
        Makes a copy of the fitness list and then returns the best fitness.
        Parameters
        - fitness: (The fitness list being considered)
    """
    fitnessCopy = fitness.copy() or []
    fitnessCopy.sort(reverse=True)
    return fitnessCopy[0]
def get_best_solution(population):
    """
        Gets the best solution in a population based on the highest fitness
        Parameters
        - population: (The Current Population we are considering) 
    """
    fitness = [calculate_fitness(individual) for individual in population]
    best_fitness = get_best_fitness(fitness)
    best_solution_position = fitness.index(best_fitness)
    return population[best_solution_position]
   

def print_board(individual):
    """
        Prints out the board for a particular individual
        Parameters
        - individual: (The individual we want to print out) 
    """
    
    for i in range(8):
        for j in range(len(individual)):
            if((i+1) == individual[j]):
                print('Q', end=' ')
            else:
                print('-', end=" ")
        print()
def genetic_algorithm(population_size,num_of_queens, mutation_rate,max_generation,target_fitness,num_of_parents):
    """
        The driver function for the whole algorithm. 
    """
    population = generate_population(population_size, num_of_queens)
    generation_count = 0
    best_fitness = 0
    best_solution = []
    print(f"initial population {population}")
    while not check_for_termination(target_fitness,best_fitness,generation_count,max_generation):
        population = create_next_generation(population,mutation_rate)
        fitness = [calculate_fitness(individual) for individual in population]
        best_fitness = get_best_fitness(fitness)
        generation_count+=1
    best_solution = get_best_solution(population)
    print(f"Best solution {28 - best_fitness}")
    return best_solution

def main():
    best_solution = genetic_algorithm(100,8,0.1, 1000, 28, 2)
    print("the best solution generated by the genetic algorithm")
    print_board(best_solution)
if __name__ == "__main__":
    main()