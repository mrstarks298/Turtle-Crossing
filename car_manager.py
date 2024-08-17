from turtle import Turtle
import random

# List of colors for the cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# Initial speed at which cars move
STARTING_MOVE_DISTANCE = 5
# Increment to increase car speed
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        # List to hold all the car objects
        self.all_cars = []
        # Speed at which the cars will move
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # Randomly decide if a new car should be created
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            # Create a new car object
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Set the size of the car
            new_car.penup()  # Lift the pen to prevent drawing lines
            new_car.color(random.choice(COLORS))  # Assign a random color to the car
            # Set a random y position for the car
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)  # Place the car on the right edge of the screen
            # Add the new car to the list of all cars
            self.all_cars.append(new_car)

    def move_cars(self):
        # Move all cars backward by the current speed
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        # Increase the car speed
        self.car_speed += MOVE_INCREMENT
