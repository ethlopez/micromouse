from mouse import Mouse
from maze import generate_maze, display_maze

if __name__ == "__main__":
    mouse = Mouse()
    mouse.check_surroundings()

    maze = generate_maze(5)
    display_maze(maze)
