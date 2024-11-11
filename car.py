import pygame
import math

from constants import *

class Car:
    def __init__(self, image, width, height, position, velocity, direction, momentum,
                 rotation, gas_acceleration, brake_acceleration, roll_friction, skid_friction, turn_factor, max_speed):
        self.image = image
        self.width = width
        self.height = height
        self.position = position
        self.velocity = velocity
        self.direction = direction
        self.momentum = momentum
        self.rotation = rotation
        self.gas_acceleration = gas_acceleration
        self.brake_acceleration = brake_acceleration
        self.roll_friction = roll_friction
        self.skid_friction = skid_friction
        self.turn_factor = turn_factor
        self.max_speed = max_speed

class Opponent(Car):
    def __init__(self, image, width, height, position, velocity, direction, momentum, rotation,
            gas_acceleration, brake_acceleration, roll_friction, skid_friction, turn_factor, max_speed,
                 difficulty):
        super().__init__(
            image, width, height, position, velocity, direction, momentum, rotation,
            gas_acceleration, brake_acceleration, roll_friction, skid_friction, turn_factor, max_speed
        )

        self.difficulty = difficulty

class Player(Car):
    def __init__(
        self, image, width, height, position, velocity, direction, momentum, rotation,
            gas_acceleration, brake_acceleration, roll_friction, skid_friction, turn_factor, max_speed):
        super().__init__(
            image, width, height, position, velocity, direction, momentum, rotation,
            gas_acceleration, brake_acceleration, roll_friction, skid_friction, turn_factor, max_speed
        )

        self.image = pygame.transform.scale(self.image, (self.width, self.height))


    def update_rotation(self, delta_time):
        keys = pygame.key.get_pressed()

        turn_speed = math.sqrt(self.velocity.x ** 2 + self.velocity.y ** 2) * self.turn_factor

        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            pass
        elif keys[pygame.K_LEFT]:
            self.rotation.radians -= turn_speed * delta_time
        elif keys[pygame.K_RIGHT]:
            self.rotation.radians += turn_speed * delta_time

        target_direction = Vector(x = math.cos(self.rotation.radians), y = math.sin(self.rotation.radians))

        turn_blend_factor = 0.05
        self.direction.x = ((1 - turn_blend_factor) * self.direction.x + turn_blend_factor * target_direction.x)
        self.direction.y = ((1 - turn_blend_factor) * self.direction.y + turn_blend_factor * target_direction.y)

        if abs(self.direction.x - target_direction.x) < MOVEMENT_ZERO_MARGIN:
            self.direction.x = target_direction.x
        if abs(self.direction.y - target_direction.y) < MOVEMENT_ZERO_MARGIN:
            self.direction.y = target_direction.y

        if abs(self.direction.x - target_direction.x) + (self.direction.y - target_direction.y) > 2:
            self.velocity.x *= self.skid_friction
            self.velocity.y *= self.skid_friction

        direction_magnitude = math.sqrt(self.direction.x ** 2 + self.direction.y ** 2)
        if direction_magnitude > 0:
            self.direction.x /= direction_magnitude
            self.direction.y /= direction_magnitude

        self.rotation.angle = -self.rotation.radians * (180 / math.pi)

    def update_position(self, delta_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if self.velocity.x > 0 and self.velocity.y > 0:
                self.velocity.x += self.gas_acceleration * delta_time
                self.velocity.y += self.gas_acceleration * delta_time
            else:
                self.velocity.x += self.brake_acceleration * delta_time
                self.velocity.y += self.brake_acceleration * delta_time
        elif keys[pygame.K_DOWN]:
            if self.velocity.x < 0 and self.velocity.y < 0:
                self.velocity.x -= self.gas_acceleration * delta_time
                self.velocity.y -= self.gas_acceleration * delta_time
            else:
                self.velocity.x -= self.brake_acceleration * delta_time
                self.velocity.y -= self.brake_acceleration * delta_time
        else:
            self.velocity.x *= self.roll_friction
            self.velocity.y *= self.roll_friction

            if abs(self.velocity.x) < MOVEMENT_ZERO_MARGIN:
                self.velocity.x = 0
            if abs(self.velocity.y) < MOVEMENT_ZERO_MARGIN:
                self.velocity.y = 0

        self.velocity.x = min(self.velocity.x, self.max_speed)
        self.velocity.y = min(self.velocity.y, self.max_speed)

        self.position.x += self.velocity.x * self.direction.x * delta_time
        self.position.y += self.velocity.y * self.direction.y * delta_time

player = Player(
    image = pygame.image.load('car.png'),
    width = 50,
    height = 50,
    position = Vector(x = WINDOW_WIDTH // 2, y = WINDOW_HEIGHT // 2),
    velocity = Vector(x = 0, y = 0),
    direction = Vector(x = 0, y = 0),
    momentum = Vector(x = 0, y = 0),
    rotation = Rotation(radians = 0, angle = 0),
    gas_acceleration = 100,
    brake_acceleration = 250,
    roll_friction = 0.98,
    skid_friction = 0.96,
    turn_factor = 0.005,
    max_speed = 500
)