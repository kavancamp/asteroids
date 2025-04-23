import pygame.mixer

try:
    pygame.mixer.init()
    laser_sound = pygame.mixer.Sound("sounds/retro-laser-1-236669.mp3")
    explode_sound = pygame.mixer.Sound("sounds/explosion-312361.mp3")
except pygame.error:
    print("⚠️  Sound system not available. Running without sound.")
    laser_sound = None
    explode_sound = None
