class Mouse:
    """
    Main class for micromouse.

    TODO: Implement coordinate and direction system (likely vectors).
    TODO: Implement physics system (ties well with vectors).
    TODO: Complete documentation for each subroutine.
    """

    # TODO: Implement a way to store mazes.
    map: list[int] = []


    def __init__(self) -> None:
        """
        Constructor for the Mouse class.

        The list self.route contains commands.
        Each command is a list of length 2:
            command[0] is the steps argument for move()
            command[1] is the angle argument for turn()

        TODO: Complete any other setup.
        """
        
        self.route: list[list[int, float]] = []


    def _info(self):
        """
        Displays metadata about mouse instance for debugging.

        TODO: Document debugging subroutine.
        """

        # TODO: Implement debugging subroutine.
        pass

    def move(self, steps: int) -> bool:
        """
        Moves the mouse forwards in the currently facing direction.
        Returns True if successfully moved forward.

        TODO: Update mouse position.
        """

        print("Moving", steps, "steps forwards...")
        return True


    def turn(self,
             angle: int | float,
             is_degrees: bool = False) -> bool:
        """
        Turns the mouse clockwise.
        Returns True if successfully turned.

        Angle is given in radians by default.
        Passing the 3rd argument as True takes angle as degrees.

        TODO: Update mouse direction.
        """

        if not is_degrees:
            # TODO: Convert angle from radians to degrees.
            pass

        print("Turning", angle, "degrees clockwise...")
        return True


    def check(self) -> bool:
        """
        Checks forwards for obstacles.
        Returns True if clear (no obstacle).
        Returns False if obstacle.

        TODO: Implement way to read mazes and check for obstacles.
        """

        print("Checking forwards for obstacles...")
        return True


    def check_surroundings(self) -> tuple[bool, bool, bool, bool]:
        """
        Checks in all 4 directions for obstacles.

        Returns a tuple, based on surroundings, a list of length 4:
            surroundings[0]: True if there is an obstacle forwards.
            surroundings[1]: True if there is an obstacle rightwards.
            surroundings[2]: True if there is an obstacle backwards.
            surroundings[3]: True if there is an obstacle leftwards.
        """

        surroundings: list[bool] = []

        for i in range(4):
            is_clear: bool = self.check()
            surroundings.append(is_clear)
            self.turn(90, True)
        
        return tuple(surroundings)
    
    
    def explore(self):
        """
        This subroutine allows the mouse to map out the maze.

        TODO: Describe the explore algorithm.
        """

        # TODO: Implement an explore algorithm.
        pass


    # Should this subroutine be separate from the class?
    # If it is part of the class, it can use instance variables.
    # If it is self-contained, it can use parameters.
    # It will likely be long and require some documentation.
    def solve(self):
        """
        This subroutine finds an optimised route through the maze.

        TODO: Describe the solve algorithm.
        """

        # TODO: Implement a solve algorithm.
        pass

