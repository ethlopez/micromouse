def get_neighbours(x : int,
                   y : int,
                   maze : list[list[bool]], 
                   diagonal_bias : bool = False) -> list[bool]:
    #returns the cells adjacent and if diagonal_bias is true, diagonal to the cell
    adjacent_indexes = [
        [y-1, x+0],
        [y+0, x+1],
        [y+1, x+0],
        [y+0, x-1]
    ]
                       
    #adds diagonals if the generator is using a diagonal_bias
    if diagonal_bias:
        adjacent_indexes.append([y-1, x-1],
                                [y+1, x-1],
                                [y-1, x+1],
                                [y+1, x+1])
        
    return adjacent_indexes

        
def is_valid_neighbour(x : int,
                         y : int,
                         maze : list[list[bool]],
                         diagonal_bias : bool = False) -> bool:

    neighbours = get_neighbours(x, y, maze, diagonal_bias)
    number_of_empty_neighbours = 0
    
    for i in range(len(neighbours)):
        if not neighbours[i]:
            number_of_empty_neighbours += 1
            
    valid = number_of_empty_neighbours == 1 and maze[y][x]
                             
    return valid
        
            
        


def generate_maze(parameter: int) -> list[int]:
    """
    Customisable maze generator.

    Specification:
    - 16x16 grid (or can be made general)
    - Defined start and endpoints
    - Parameter(s) to control complexity
    - Parameter(s) to control diagonals

    TODO: Finish specification.

    TODO: Add parameters.
    TODO: Document maze generating algorithm.
    """

    #define the maze open cell resolution
    resolution = 16

    #defines the number of cells included
    #e.g.
    #a maze with a resolution of 2x2 may look like this
    #    1 2
    #   ┌─┬─┐
    # 1 │A│B│
    #   │ │ │
    # 2 │C D│
    #   └───┘
    #but when walls are regarded as individual tiles will look like this
    #   12345
    # 1 █████
    # 2 █A█B█
    # 3 █ █ █
    # 4 █C D█
    # 5 █████
    maze_cell_length = (resolution*2)+1

    #if the maze generator will try and use diagonals
    diagonal_bias = True

    #define starting (top left corner) and ending point (center) of the maze
    start_position = [1, 1]
    end_position = [maze_cell_length/2, maze_cell_length/2]
    
    #define the maze
    maze = []
    
    #each of the mazes values are represented by a boolean
    #each value is used to represents the different walls on a tile of the maze
    #each tiles bits corrisponds to if there is a wall on at tile
    
    #assign the decimal values of the maze 
    #all maze tiles start as walls
  
    for y in range(maze_cell_length):
        maze.append([])
        for x in range(maze_cell_length):
            maze.append(True)


    #sets the boolean to let the generator when it has reached a stop
    maze_finished = False

    #sets a list of cells that can be added to the maze
    x = start_position[0]
    y = start_position[1]
    expansion_cells = get_neighbours(x, y, diagonal_bias, maze)
    for i in range(len(expansion_cells)):
        expansion_cells[i]

    #while the maze it not finished
    while not maze_finished:
      pass
                
      
      
    
    # TODO: Implement maze generating algorithm.
    return [parameter, parameter, parameter]


def display_maze(maze: list[int]) -> None:
    """
    Customisable maze displayer.

    Specification:
    - 16x16 grid (or can be made general)
    - Defined start and end points
    - Parameters to control features (walls, start, end)

    TODO: Finish specification.

    TODO: Add parameters.
    TODO: Document subroutine.
    """

    # TODO: Implement subroutine.
    print(maze)
