from turtle import Turtle

# Constants for player movement and game setup
STARTING_POSITION = (0, -280)  # Initial position of the player at the bottom of the screen
MOVE_DISTANCE = 10  # Distance the player moves with each key press
FINISH_LINE_Y = 280  # Y-coordinate of the finish line

class Player(Turtle):

    def __init__(self):
        super().__init__()
        # Set the turtle's appearance and initial state
        self.shape("turtle")  # Set the shape to a turtle
        self.penup()  # Lift the pen to avoid drawing lines
        self.go_to_start()  # Place the player at the starting position
        self.setheading(90)  # Face the turtle upward (toward the finish line)

    def go_up(self):
        # Move the player forward (upward) by the specified distance
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        # Send the player back to the starting position
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        # Check if the player has crossed the finish line
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
