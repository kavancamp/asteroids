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
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            if self.explode_sound:
                self.explode_sound.play()
            return
        for _ in range(30):  # spawn 20 particles
            self.particle_group.add(Particle(self.position))

        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        

        # Spawn two new asteroids with new velocities and radius
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2
       
        # Remove the original asteroid
        self.kill()