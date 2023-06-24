# Natural Selection Simulator

### General Concept
This library simulator the process of natural selection in a 2D digital world. The basic structure is base on the object creature that can move around in a matrix 2D. The creature can move in any of the 8 spaces around it available base on a certain probability given for each movement (genes). After a while of simulation the criteria of selection is applied and only the creatures within the area select as safe survive and have the chance to reproduce. In the next simulation, the next generation of creatures will be born base on the survivors.

### Code Structure

- Creatures
* Have 8 genes related to each movement. Each gene is a probability (float between 0 and 1)

- Simulator
* Receives the inputs of the simulation: length of the world, selection criteria, Number of creatures to be create, number of generations to run, number of decisions per generation
* Populate the world matrix with the objects of the creatures
* For each generation, run the decisions necessary
* Apply the selection criteria
* reborn the new creatures base on the genes of the survivors
* populate the world again and run the next generation