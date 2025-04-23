import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from particle import Particle
from sound_fx import explode_sound

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):  # <-- Accept x and y as arguments
        super().__init__(x, y, radius)
    particle_group = None 
    explode_sound = None

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        # Particle burst
        for _ in range(10 if self.radius <= ASTEROID_MIN_RADIUS else 30):
            self.particle_group.add(Particle(self.position))

        # Small asteroids die not split apart
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        # Play sound if available
        if self.explode_sound:
            self.explode_sound.play()

        # Calculate new velocities and size
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # instantiate and assign velocity
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = velocity1
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = velocity2

        self.kill()
