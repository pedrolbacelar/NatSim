"""
- Simulator
* Receives the inputs of the simulation: length of the world, selection criteria, Number of creatures to be create, number of generations to run, number of decisions per generation
* Populate the world matrix with the objects of the creatures
* For each generation, run the decisions necessary
* Apply the selection criteria
* reborn the new creatures base on the genes of the survivors
* populate the world again and run the next generation
"""
from components import Creature, Gene, World
from helper import Helper
import random
import time

class Simulator():
    def __init__(self, world_dimension= (128, 128), number_of_creatures= 25, number_of_generations= 10, number_of_movements= 100, selection_criteria= "left-side", plot_mode = "last"):
        #--- Parameters
        self.world_dimension = world_dimension
        self.length = world_dimension[0]
        self.width = world_dimension[1]
        self.number_of_creatures = number_of_creatures
        self.number_of_generations = number_of_generations
        self.number_of_movements = number_of_movements
        self.selection_criteria = selection_criteria
        self.plot_mode = plot_mode
        self.helper = Helper()

        #--- Initialization
        self.initiate_world()

    def initiate_world(self):
        # Create Creatures
        self.creatures = []
        positions_taken = []
        position_available = False

        for i in range(self.number_of_creatures):
            # Create the genes
            gene_prob = [random.random() for i in range(8)]
            gene = Gene(gene_prob)

            # Create the position
            while position_available == False:
                position = [random.randint(0, self.length - 1), random.randint(0, self.width - 1)]
                if position not in positions_taken:
                    position_available = True
                else:
                    position_available = False

            #--- Position Control
            positions_taken.append(position)
            position_available = False


            # Create the creature
            creature = Creature(i, gene, position)
            self.creatures.append(creature)


        # Create the world
        self.world = World(self.world_dimension[0], self.world_dimension[1], self.creatures)

        # Populate the world
        self.world.populate_world()

    def run(self):
        # Run the simulation
        self.helper.printer("---- Simulation Started ----", 'green')
        starting_time = self.helper.get_time_now()[1]

        for i in range(self.number_of_generations):

            # Run the decisions
            for j in range(self.number_of_movements):
                #--- Move creatures
                self.world.move_creatures()
            
            self.helper.printer(f" --- Generation {i + 1} finished ---")
            
            #--- Apply selection criteria
            self.saved_genes = self.world.apply_selection(self.selection_criteria)

            #--- Reborn the new creatures
            self.creatures = self.world.create_creatures(saved_genes= self.saved_genes, number_of_creatures= self.number_of_creatures)

            #--- Populate the world again
            self.world.populate_world()




        # ------------ End of Simulation ------------
        ending_time = self.helper.get_time_now()[1]
        simulation_time = ending_time - starting_time
        self.helper.printer("---- Simulation Finished ----", 'green')
        self.helper.printer("Simulation Time: " + str(simulation_time) + " seconds")
        self.helper.printer(f"Percentage of Survivors: {round((len(self.saved_genes) / self.number_of_creatures) * 100, 2)}%")

        if self.plot_mode == "last":
            self.world.plot_world_evolution(number_of_movements= self.number_of_movements)
        
        else:
            self.world.plot_world_evolution()

        



    #--------- Get Functions ------------
    def get_creatures(self):
        return self.creatures
    def get_world(self):
        return self.world