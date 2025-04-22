import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):  # <-- Accept x and y as arguments
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)