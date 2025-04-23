import pygame
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self, position, color=(255, 255, 255)):
        super().__init__()
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)) * random.randint(50, 100)
        self.lifetime = random.uniform(0.3, 0.8)
        self.radius = random.randint(1, 3)
        self.color = color

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, self.position, self.radius)
