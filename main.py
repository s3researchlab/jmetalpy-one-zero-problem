from jmetal.operator.crossover import SPXCrossover
from jmetal.operator.mutation import BitFlipMutation
from jmetal.operator.selection import BinaryTournamentSelection
from jmetal.util.termination_criterion import StoppingByEvaluations

from OneZeroProblem import OneZeroProblem
from GA import GA

ARRAY_SIZE = 100
POPULATION_SIZE = 100
GENERATIONS = 2

def main():
    
    problem = OneZeroProblem(ARRAY_SIZE)
    
    solution = problem.create_solution()
    
    print(problem.evaluate(solution))
    
    algorithm = GA(
        problem=problem,
        population_size=POPULATION_SIZE,
        offspring_population_size=POPULATION_SIZE,
        mutation=BitFlipMutation(0.005),
        crossover=SPXCrossover(0.9),
        selection=BinaryTournamentSelection(),
        termination_criterion=StoppingByEvaluations(max_evaluations=POPULATION_SIZE*GENERATIONS)
    )
    
    algorithm.run()
    
    print(algorithm.result())
    # print(algorithm.get_best_solutions())
    
    output = open("output.csv", "w")  # write mode
    output.write("generation, best_value\n")
        
    for index, value in enumerate(algorithm.best_values):
        output.write("{0},{1}\n".format(index+1, value))
        
    output.close()
    
if __name__ == "__main__":
    main()