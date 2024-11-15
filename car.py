import pygame
import math

from constants import *

class Car:
    def __init__(self, image, width, height, position, velocity, direction,
                 rotation, gas_acceleration, brake_acceleration, roll_acceleration, skid_acceleration, min_turn_radius, turn_factor, max_turn_speed, max_speed):
        self.image = image
        self.width = width
        self.height = height
        self.position = position
        self.velocity = velocity
        self.direction = direction
        self.rotation = rotation
        self.gas_acceleration = gas_acceleration
        self.brake_acceleration = brake_acceleration
        self.roll_acceleration = roll_acceleration
        self.skid_acceleration = skid_acceleration
        self.min_turn_radius = min_turn_radius
        self.turn_factor = turn_factor
        self.max_turn_speed = max_turn_speed
        self.max_speed = max_speed

class Opponent(Car):
    def __init__(self, image, width, height, position, velocity, direction, rotation,
                 gas_acceleration, brake_acceleration, roll_acceleration, skid_acceleration, min_turn_radius, turn_factor, max_turn_speed, max_speed,
                 difficulty):
        super().__init__(
            image, width, height, position, velocity, direction, rotation,
            gas_acceleration, brake_acceleration, roll_acceleration, skid_acceleration, min_turn_radius, turn_factor, max_turn_speed, max_speed
        )

        self.difficulty = difficulty

class Player(Car):
    def __init__(
        self, image, width, height, position, velocity, direction, rotation,
            gas_acceleration, brake_acceleration, roll_acceleration, skid_acceleration, min_turn_radius, turn_factor, max_turn_speed, max_speed):
        super().__init__(
            image, width, height, position, velocity, direction, rotation,
            gas_acceleration, brake_acceleration, roll_acceleration, skid_acceleration, min_turn_radius, turn_factor, max_turn_speed, max_speed
        )

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def update_rotation(self, delta_time, current_track):
        keys = pygame.key.get_pressed()

        turn_radius = math.sqrt(self.velocity.x ** 2 + self.velocity.y ** 2) * self.turn_factor
        turn_radius = max(turn_radius, self.min_turn_radius * PIXEL_TO_SCREEN_FACTOR)

        turn_speed = math.sqrt(self.velocity.x ** 2 + self.velocity.y ** 2) / turn_radius if turn_radius > 0 else 0

        # Get input
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            pass
        elif keys[pygame.K_LEFT]:
            self.rotation.radians -= turn_speed * delta_time
        elif keys[pygame.K_RIGHT]:
            self.rotation.radians += turn_speed * delta_time

        self.rotation.angle = -self.rotation.radians * (180 / math.pi)

        # Get target direction vector based on where the car is pointing
        target_direction = Vector(x = math.cos(self.rotation.radians), y = math.sin(self.rotation.radians))

        # Set travel direction to target direction based on a linear interpolation equation
        # direction = ((1 - turn blending) x direction + turn blending x target direction)
        # turn_blend_factor is how fast travel direction equals target direction
        self.direction.x = ((1 - current_track.friction) * self.direction.x + current_track.friction * target_direction.x)
        self.direction.y = ((1 - current_track.friction) * self.direction.y + current_track.friction * target_direction.y)

        if abs(self.direction.x - target_direction.x) + (self.direction.y - target_direction.y) > 2:
            self.velocity.x *= self.skid_acceleration #
            self.velocity.y *= self.skid_acceleration # Apply skid friction if target direction and travel direction are more than 90 degrees from each other

        # Makes sure direction vector is equal to direction magnitude
        direction_magnitude = math.sqrt(self.direction.x ** 2 + self.direction.y ** 2)
        if direction_magnitude > 0:
            self.direction.x /= direction_magnitude
            self.direction.y /= direction_magnitude

    def update_position(self, delta_time, current_track):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            pass
        elif keys[pygame.K_UP]:
            if self.velocity.x > 0 and self.velocity.y > 0: # Check if moving forward
                self.velocity.x += self.gas_acceleration * delta_time
                self.velocity.y += self.gas_acceleration * delta_time
            else: # Is moving backwards
                self.velocity.x += self.brake_acceleration * delta_time
                self.velocity.y += self.brake_acceleration * delta_time
        elif keys[pygame.K_DOWN]:
            if self.velocity.x < 0 and self.velocity.y < 0: # Check if moving backwards
                self.velocity.x -= self.gas_acceleration * delta_time
                self.velocity.y -= self.gas_acceleration * delta_time
            else: # Is moving forwards
                self.velocity.x -= self.brake_acceleration * delta_time
                self.velocity.y -= self.brake_acceleration * delta_time
        else: # Up/Down arrow keys are not down
            self.velocity.x *= self.roll_acceleration #
            self.velocity.y *= self.roll_acceleration # Apply friction when rolling

            if abs(self.velocity.x) < MOVEMENT_ZERO_MARGIN:
                self.velocity.x = 0
            if abs(self.velocity.y) < MOVEMENT_ZERO_MARGIN: # Check if velocity is near zero
                self.velocity.y = 0 #if below a certain margin, set to zero

        self.velocity.x = max(min(self.velocity.x, self.max_speed), -self.max_speed) #
        self.velocity.y = max(min(self.velocity.y, self.max_speed), -self.max_speed) # Max speed

        self.position.x += self.velocity.x * self.direction.x * delta_time #
        self.position.y += self.velocity.y * self.direction.y * delta_time # Update position

player = Player(
    image = pygame.image.load('red_car.png'), # Car image path
    width = pygame.image.load('red_car.png').get_width() * PIXEL_TO_SCREEN_FACTOR, # Car width so it retains its aspect with rescale
    height = pygame.image.load('red_car.png').get_height() * PIXEL_TO_SCREEN_FACTOR, # Car height so it retains its aspect with rescale
    position = Vector(x = 0, y = 0), # Position in world
    velocity = Vector(x = 0, y = 0), # Forward velocity (positive if moving forward from the car's point of view, negative if moving backwards from car's point of view)
    direction = Vector(x = 0, y = 0), # The direction that the car is currently moving in (-1 to 1) and multiplies by velocity to get new position
    rotation = Rotation(radians = 0, angle = 0), # The current rotation of the car in radians and angles
    gas_acceleration = 80, # Acceleration when pressing gas button
    brake_acceleration = 250, # Acceleration when pressing brake button
    roll_acceleration = 0.98, # Acceleration when acceleration buttons pressed
    skid_acceleration = 0.96, # Acceleration when burning out (Target direction + Travel direction > 90)
    min_turn_radius = 30,
    turn_factor = 0.5, # The rate at which cars turn
    max_turn_speed = 3, # The maximum turn speed
    max_speed = 600 # The maximum velocity
)