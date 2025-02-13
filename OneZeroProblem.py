import random

from jmetal.core.problem import Problem
from jmetal.core.solution import BinarySolution

class OneZeroProblem(Problem[BinarySolution]):
    
    def __init__(self, array_length: int):
        super().__init__()
        
        self.array_length = array_length

    def evaluate(self, solution: BinarySolution) -> BinarySolution:
        
        ones_count = sum(solution.variables[0])  # Count ones
        
        solution.objectives[0] = ones_count  # Fitness = number of ones
        
        return solution

    def create_solution(self) -> BinarySolution:
        
        # Generate random binary solution
        new_solution = BinarySolution(
            number_of_variables=self.number_of_variables(), 
            number_of_objectives=self.number_of_objectives()
        )
        
        new_solution.variables = [[random.choice([True, False]) for _ in range(self.number_of_variables())]]
        
        return new_solution
    
    def name(self) -> str:
        return "OneZeroProblem"

    def number_of_objectives(self) -> int:
        return 1

    def number_of_variables(self) -> int:
        return self.array_length
    
    def number_of_constraints(self) -> int:
        return 0