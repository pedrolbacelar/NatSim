from Simulator import Simulator

simulator = Simulator(
    world_dimension= (128, 128),
    number_of_creatures= 100,
    number_of_generations= 30,
    number_of_movements= 500,
    selection_criteria= "left-side",
    plot_mode = "last"
)
simulator.run()