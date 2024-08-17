import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set the screen size
screen.tracer(0)  # Turn off automatic screen updates for better control

# Create instances of the Player, CarManager, and Scoreboard classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for key presses
screen.listen()
screen.onkey(player.go_up, "Up")  # Move the player up when the "Up" arrow key is pressed

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Slow down the game loop slightly for smoother gameplay
    screen.update()  # Manually update the screen

    # Create new cars and move all existing cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # If the car is very close to the player
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display the "Game Over" message

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()  # Reset the player to the starting position
        car_manager.level_up()  # Increase car speed as difficulty increases
        scoreboard.increase_level()  # Update and display the player's level

# Exit the game when the screen is clicked
screen.exitonclick()
