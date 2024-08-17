from turtle import Turtle

# Font settings for the scoreboard
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1  # Initialize the game level to 1
        self.hideturtle()  # Hide the turtle shape (only show text)
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(-280, 250)  # Position the scoreboard at the top-left of the screen
        self.update_scoreboard()  # Display the initial level

    def update_scoreboard(self):
        # Clear the previous level and write the updated level
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        # Increase the level and update the scoreboard display
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        # Display the "Game Over" message at the center of the screen
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER", align="center", font=FONT)
