import pygame

class Race:
    def __init__(self, friction):
        self.friction = friction # <0.001 to 1 (0 = 0% blending each frame, 1 = 100% blending each frame)
        #self.obstacles = obstacles

class Obstacle:
    def __init__(self, position, width, height, color = None, obstacle_rect = None):
        self.position = position
        self.width = width
        self.height = height
        self.color = color
        self.obstacle_rect = obstacle_rect

    def get_rect(self):
        self.obstacle_rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

    def create_obstacle(self):
        pass

    def destroy_obstacle(self):
        pass

race = Race(0.05)

current_track = race