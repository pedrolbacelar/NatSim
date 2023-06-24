"""
### General Concept
This library simulator the process of natural selection in a 2D digital world. The basic structure is base on the object creature that can move around in a matrix 2D. The creature can move in any of the 8 spaces around it available base on a certain probability given for each movement (genes). After a while of simulation the criteria of selection is applied and only the creatures within the area select as safe survive and have the chance to reproduce. In the next simulation, the next generation of creatures will be born base on the survivors.

### Code Structure

- Creatures
* Have 8 genes related to each movement. Each gene is a probability (float between 0 and 1)
* id

- Simulator
* Receives the inputs of the simulation: length of the world, selection criteria, Number of creatures to be create, number of generations to run, number of decisions per generation
* Populate the world matrix with the objects of the creatures
* For each generation, run the decisions necessary
* Apply the selection criteria
* reborn the new creatures base on the genes of the survivors
* populate the world again and run the next generation
"""

import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Gene():
    """
    gene_vector: [upper, upper_right, right, lower_right, lower, lower_left, left, upper_left]
    """
    def __init__(self, gene_prob):
        self.gene_prob = gene_prob
        self.gene_dict = {
            "upper": gene_prob[0],
            "upper_right": gene_prob[1],
            "right": gene_prob[2],
            "lower_right": gene_prob[3],
            "lower": gene_prob[4],
            "lower_left": gene_prob[5],
            "left": gene_prob[6],
            "upper_left": gene_prob[7]
        }

    def gene_activation(self):
        # Get parameters
        movements = list(self.gene_dict.keys())
        probabilities = list(self.gene_dict.values())

        # Get the movement base on the probability
        chosen_movement = random.choices(movements, weights=probabilities, k=1)

        return chosen_movement[0]
    

class Creature():
    def __init__(self, id, gene, position, verbose= False):
        self.id = id
        self.gene = gene
        self.position = position
        self.verbose = verbose

    def move(self):
        """ Make the choice of movement """
        chosen_movement = self.gene.gene_activation()

        #--- Translate decision to the matrix position
        if chosen_movement == "upper":
            position = [self.position[0], self.position[1] + 1]
        elif chosen_movement == "upper_right":
            position = [self.position[0] + 1, self.position[1] + 1]
        elif chosen_movement == "right":
            position = [self.position[0] + 1, self.position[1]]
        elif chosen_movement == "lower_right":
            position = [self.position[0] + 1, self.position[1] - 1]
        elif chosen_movement == "lower":
            position = [self.position[0], self.position[1] - 1]
        elif chosen_movement == "lower_left":
            position = [self.position[0] - 1, self.position[1] - 1]
        elif chosen_movement == "left":
            position = [self.position[0] - 1, self.position[1]]
        elif chosen_movement == "upper_left":
            position = [self.position[0] - 1, self.position[1] + 1]
        

        if self.verbose:
            print("Creature {} is moving to {}".format(self.id, chosen_movement))

        return position
    
    def get_position(self):
        return self.position
    
    def get_genes(self):
        return self.gene


class World():
    def __init__(self, length, width, creatures):
        self.length = length
        self.width = width
        self.world_matrix_current = [[0 for x in range(length)] for y in range(width)]
        self.world_history = []
        self.creatures = creatures

    def populate_world(self):
        """ Populate the world with creatures """
        # Populate the world
        for creature in self.creatures:
            self.world_matrix_current[creature.position[0]][creature.position[1]] = creature

        # Save the world
        self.world_history.append(self.world_matrix_current)

    def move_creatures(self):
        """ Move the creatures """
        # Create a new world matrix
        self.world_matrix_next = [[0 for x in range(self.length)] for y in range(self.width)]

        # Move the creatures
        for creature in self.creatures:
            position_possible = False
            try_counter = 0
            old_position = creature.get_position()

            while not position_possible:
                # Get the movement
                new_position = creature.move()

                # Check if the position is possible
                if new_position[0] >= 0 and new_position[0] < self.length and new_position[1] >= 0 and new_position[1] < self.width and self.world_matrix_next[new_position[0]][new_position[1]] == 0:
                    position_possible = True

                try_counter += 1

                if try_counter > 5:
                    #print(" - Creature {} is stuck".format(creature.id))
                    new_position = old_position
                    break

            # Update the world matrix
            self.world_matrix_next[new_position[0]][new_position[1]] = creature

            # Update the creature position
            creature.position = new_position

        print(f" - Creature {creature.id} moved to {creature.position}")

        # Save the world
        self.world_history.append(self.world_matrix_next)

    def apply_selection(self, selection_criteria):
        """
        Apply Selection Criteria 
        Criterias: left-side, right-side, upper-side, lower-side

        Take the last matrix of worlds and save only creatures that are according to the criteria
        For example, lef-side criteria save the creatures that are untill 35% close to the left side of the world
        """
        self.saved_creatures = []
        closeness_percentage = 0.1

        if selection_criteria == "left-side":
            # Get the left-side creatures
            safety_zone = int(self.width * closeness_percentage)
            for row in range(self.length):
                for col in range(safety_zone, self.width):
                    if self.world_matrix_next[row][col] != 0:
                        self.saved_creatures.append(self.world_matrix_next[row][col])

        if selection_criteria == "right-side":
            # Get the right-side creatures
            safety_zone = int(self.width * closeness_percentage)
            for row in range(self.length):
                for col in range(0, self.width - safety_zone):
                    if self.world_matrix_next[row][col] != 0:
                        self.saved_creatures.append(self.world_matrix_next[row][col])

        #--- Extrac survivors genes
        saved_genes = []
        for creatures in self.saved_creatures:
            saved_genes.append(creatures.get_genes())

        return saved_genes

    def create_creatures(self, number_of_creatures= False, saved_genes= False, ):
        # Create Creatures
        self.creatures = []
        positions_taken = []
        position_available = False
        genes_kid = []

        if number_of_creatures and saved_genes:
            number_gap = number_of_creatures - len(saved_genes)
            for i in range(number_gap):
                genes_kid.append(saved_genes[i])

            saved_genes = saved_genes + genes_kid
        
        for i in range(number_of_creatures):
            # Create the genes
            if saved_genes:
                gene = saved_genes[i]
            else:
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

        return self.creatures

    def set_creatures(self, creatures):
        self.creatures = creatures

    def plot_world_evolution(self, number_of_movements= False):
        """ Plot the world evolution """
        fig, ax = plt.subplots()
        rows = self.length
        cols = self.width

        if number_of_movements:
            world_to_plot = self.world_history[-number_of_movements:]
        else:
            world_to_plot = self.world_history

        def update(frame):
            ax.cla()  # Clear the previous frame
            ax.set_aspect('equal')
            ax.set_xlim([0, cols - 1])
            ax.set_ylim([0, rows - 1])
            ax.axis('off')

            world = world_to_plot[frame]  # Get the world matrix for the current frame

            for row in range(rows):
                for col in range(cols):
                    if world[row][col] != 0:
                        ax.plot(col, rows - 1 - row, 'bo', markersize=5)

        # Create the animation
        animation = FuncAnimation(fig, update, frames=len(world_to_plot), interval=0.0001, repeat=False)

        plt.show()
    
