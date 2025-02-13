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
        termination_criterion
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
    
    def init_progress(self):
        super().init_progress()
        
        self.best_values.append(self.solutions[0].objectives[0])
    
    def update_progress(self):
        super().update_progress()
        
        self.best_values.append(self.solutions[0].objectives[0])