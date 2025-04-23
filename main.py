import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shots

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # create groups
    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawables) #tells player to add itself to groups when initialized
    Asteroid.containers = (asteroids, updatable, drawables) #every instance of asteroid added automatically
    AsteroidField.containers = updatable
    Shots.containers = (updatable, drawables, shots)
    asteroid_field = AsteroidField()
    # Instantiate game objects
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2) #instantiate player
    
    

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        # Update player input/logic
        #player.update(dt)
        updatable.update(dt) #update all updateable objects
        # collision check
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                pygame.quit()
                exit()
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.kill()

        # Clear screen/black
        screen.fill((0, 0, 0))
        # draw drawable objects
        for drawable in drawables:
            drawable.draw(screen)
        # update display
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
    pygame.quit()


if __name__ == "__main__":
    main()