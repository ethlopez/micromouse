from mouse import Mouse
from maze import generate_maze, display_maze

if __name__ == "__main__":
    maze = generate_maze(5)
    display_maze(maze)

    mouse = Mouse(maze)
    mouse.check_surroundings()
