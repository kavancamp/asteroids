import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shots
from particle import Particle


def restart_screen(screen):
    font = pygame.font.Font(None, 48)
    text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
    rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.fill((0, 0, 0))
    screen.blit(text, rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

def fade_screen(screen, fade_in=False, duration=1000):
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.fill((0, 0, 0))
    clock = pygame.time.Clock()
    steps = 30
    for i in range(steps + 1):
        alpha = int((i / steps) * 255)
        if fade_in:
            alpha = 255 - alpha
        overlay.set_alpha(alpha)
        screen.blit(overlay, (0, 0))
        pygame.display.flip()
        clock.tick(1000 // (duration // steps))


def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    font = pygame.font.Font(None, 36)
    win_font = pygame.font.Font(None, 80)

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    particles = pygame.sprite.Group()

    Player.containers = (updatable, drawables)
    Asteroid.containers = (asteroids, updatable, drawables)
    AsteroidField.containers = updatable
    Shots.containers = (updatable, drawables, shots)
    Asteroid.particle_group = particles

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    fade_screen(screen, fade_in=True)

    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

        updatable.update(dt)
        particles.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
    
                # Draw background and message
                screen.fill((0, 0, 0))
                text = win_font.render("YOU'RE DEAD!", True, (255, 0, 0))  # Red for drama
                screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
                pygame.display.flip()

                # Hold message on screen
                pygame.time.wait(2000)

                # Fade out to black
                fade_screen(screen, fade_in=False)
                return

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
                    score += 1
                    break

        screen.fill((0, 0, 0))
        screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))

        for drawable in drawables:
            drawable.draw(screen)
        for p in particles:
            p.draw(screen)

        if score >= 15:
            text = win_font.render("WINNER!!", True, (255, 255, 255))
            screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
            pygame.display.flip()

            pygame.time.wait(1000)  # short pause
            fade_screen(screen, fade_in=False)  # fade out
            return

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()

def main():
    while True:
        game_loop()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        restart_screen(screen)

            

if __name__ == "__main__":
    main()