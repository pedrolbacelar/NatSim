# Natural Selection Simulator

This is a library that simulates the process of natural selection in a 2D digital world. The simulator is based on the concept of creatures that can move around in a 2D matrix. These creatures have genes that determine their movement probabilities. The simulation progresses over multiple generations, with selection criteria determining which creatures survive and reproduce.

## General Concept

The natural selection simulator operates in a 2D digital world represented by a matrix. The fundamental unit in this world is the creature. Each creature has the ability to move in any of the eight spaces surrounding it, based on probabilities defined by its genes. These genes represent the likelihood of choosing a particular movement direction. The simulation progresses through multiple generations, applying selection criteria to determine which creatures survive and have the opportunity to reproduce.

---

## Example

#### Before "Right Selection"

https://github.com/pedrolbacelar/NatSim/assets/72768576/1251b23f-4e7c-43d1-9d1a-c36ae73c37fe

#### After "Rigth Selection"
(After 10 generation selecting only creature on the rigth of world)

https://github.com/pedrolbacelar/NatSim/assets/72768576/ea129492-2eb9-4d3c-9e1c-262d90c7f0b0

---

## How to Play

To play the natural selection simulator, follow these steps:

1. Import the Simulator module:
```python
from Simulator import Simulator
```

2. Create an instance of the Simulator class, specifying the desired parameters:
```python
simulator = Simulator(
    world_dimension=(128, 128),
    number_of_creatures=100,
    number_of_generations=30,
    number_of_movements=500,
    selection_criteria="left-side",
    plot_mode="last"
)
```
- `world_dimension`: The dimensions of the 2D world matrix (e.g., (128, 128)).
- `number_of_creatures`: The initial number of creatures to be created in the world.
- `number_of_generations`: The total number of generations the simulation will run.
- `number_of_movements`: The number of movement decisions made by each creature in a generation.
- `selection_criteria`: The criteria used to determine which creatures survive and reproduce.
- `plot_mode`: The mode for displaying the simulation plot. Options include "last" (show the plot after the last generation) or "each" (show the plot after each generation).

3. Run the simulation:
```python
simulator.run()
```

4. Observe the simulation as it progresses through the generations. The creatures will move according to their genes, and the selection criteria will determine which creatures survive and reproduce.

5. After the simulation finishes, the plot will be displayed according to the specified `plot_mode`. If `plot_mode` is set to "last", the plot will show the final generation. If `plot_mode` is set to "each", the plot will show the progression of the generations.

6. Analyze the results and explore the evolutionary dynamics observed in the simulation.

Example usage:
```python
from Simulator import Simulator

simulator = Simulator(
    world_dimension=(128, 128),
    number_of_creatures=100,
    number_of_generations=30,
    number_of_movements=500,
    selection_criteria="left-side",
    plot_mode="last"
)
simulator.run()
```

Enjoy playing with the natural selection simulator and uncovering the fascinating dynamics of evolution!

---

## Code Structure

The codebase is structured into two main components: **Creatures** and the **Simulator**.

### Creatures

Creatures are the objects that inhabit the 2D digital world. Each creature possesses eight genes, each corresponding to a specific movement direction. The genes are represented as floating-point numbers between 0 and 1, indicating the probability of choosing a particular movement direction.

### Simulator

The Simulator orchestrates the natural selection simulation process. It accepts various inputs to configure the simulation:

- **World Length**: The length of the 2D world matrix.
- **Selection Criteria**: The criteria used to determine which creatures survive and reproduce.
- **Number of Creatures**: The initial number of creatures to be created in the world.
- **Number of Generations**: The total number of generations the simulation will run.
- **Number of Decisions per Generation**: The number of movement decisions made by each creature in a generation.

The main steps of the simulation process are as follows:

1. The world matrix is populated with the initial set of creatures based on the specified number.
2. For each generation, the required number of movement decisions is made by each creature.
3. The selection criteria are applied to determine which creatures survive and have the chance to reproduce.
4. The new generation of creatures is born based on the genes of the survivors from the previous generation.
5. The world matrix is populated with the new generation of creatures.
6. Steps 2-5 are repeated for the specified number of generations.

## Conclusion

The natural selection simulator provides a framework for studying the process of natural selection in a digital environment. By manipulating the genes of the creatures and adjusting the selection criteria, you can observe how different factors impact the survival and evolution of the population. Use the provided code structure and example usage as a starting point to explore and experiment with various scenarios and research questions related to natural selection.
