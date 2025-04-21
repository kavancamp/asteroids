import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        # Update player input/logic
        player.update(dt)
        # Clear screen with black 
        screen.fill((0, 0, 0))
        # draw player
        player.draw(screen)
        # update display
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
    pygame.quit()


if __name__ == "__main__":
    main()