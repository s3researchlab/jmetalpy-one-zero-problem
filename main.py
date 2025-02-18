from jmetal.operator.crossover import SPXCrossover
from jmetal.operator.mutation import BitFlipMutation
from jmetal.operator.selection import BinaryTournamentSelection
from jmetal.util.termination_criterion import StoppingByEvaluations

from OneZeroProblem import OneZeroProblem
from GA import GA

ARRAY_SIZE = 10
POPULATION_SIZE = 100
GENERATIONS = 10

def convertArrayToSolution(problem, array):
    
    if problem.array_length != len(array):
        raise ValueError("Array length is different")
    
    solution = problem.create_solution()
   
    variables = []
   
    for x in array: 
        if x == 1:
            variables.append(True)
        else:
            variables.append(False)
            
    solution.variables = [variables]   
    
    return solution

def convertMatrixToSolutions(problem, matrix):
    
    solutions = []
    
    for array in matrix: 
        solutions.append(convertArrayToSolution(problem, array))
    
    return solutions

def main():
    
    problem = OneZeroProblem(ARRAY_SIZE)
    
    population = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    
    initial_population = convertMatrixToSolutions(problem, population)
    
    POPULATION_SIZE = len(initial_population)
    
    algorithm = GA(
        problem=problem,
        population_size=POPULATION_SIZE,
        offspring_population_size=POPULATION_SIZE,
        mutation=BitFlipMutation(0.005),
        crossover=SPXCrossover(0.9),
        selection=BinaryTournamentSelection(),
        termination_criterion=StoppingByEvaluations(max_evaluations=POPULATION_SIZE*GENERATIONS),
        initial_population= initial_population
    )
    
    algorithm.run()
    
    print(algorithm.result())
    
    output = open("output.csv", "w")  # write mode
    output.write("generation, best_value\n")
        
    for index, value in enumerate(algorithm.best_values):
        output.write("{0},{1}\n".format(index+1, value))
        
    output.close()
    
if __name__ == "__main__":
    main()