from jmetal.algorithm.singleobjective import GeneticAlgorithm

class GA(GeneticAlgorithm):
    
    def __init__(
        self,
        problem,
        population_size,
        offspring_population_size,
        mutation,
        crossover,
        selection,
        termination_criterion,
        initial_population=None
    ):
        super().__init__(
            problem,
            population_size,
            offspring_population_size,
            mutation,
            crossover,
            selection,
            termination_criterion
        )
        self.best_values = []  
        self.initial_population = initial_population
    
    def init_progress(self):
        super().init_progress()
        
        self.best_values.append(self.solutions[0].objectives[0])
    
    def update_progress(self):
        super().update_progress()
        
        self.best_values.append(self.solutions[0].objectives[0])
        
    def create_initial_solutions(self):
        
        if self.initial_population is None: 
            return super().create_initial_solutions()
        else:
            return self.initial_population
