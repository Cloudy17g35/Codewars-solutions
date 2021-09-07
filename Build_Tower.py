def tower_builder(n_floors):
    return [('*' * x).center(n_floors * 2 - 1) for x in range(1, 2 * n_floors , 2)]
