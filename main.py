import pygame
from Player import Player
import DEFAULT

pygame.init()

clock = pygame.time.Clock()

# initialisation de pygame au lancement
pygame.init()

# définir une clock
clock = pygame.time.Clock()

# on crée la fenêtre du jeu
window = pygame.display.set_mode(DEFAULT.window_size)
pygame.display.set_caption(DEFAULT.window_name)
pygame.display.set_icon(pygame.image.load(DEFAULT.window_icon))

# pygame.mixer.music.load(DEFAULT.path_music)  # import du fichier
# pygame.mixer.music.play()  # on joue le fichier
# pygame.mixer.music.set_volume(DEFAULT.music_level)

# object_ground = Ground() terrain

background = pygame.image.load(DEFAULT.background_1)
background_2 = pygame.image.load(DEFAULT.background_2)
background_3 = pygame.image.load(DEFAULT.background_3)
background_r = pygame.transform.scale(background, (DEFAULT.window_width, DEFAULT.window_height))
background_2_r = pygame.transform.scale(background_2, (DEFAULT.window_width, DEFAULT.window_height))
background_3_r = pygame.transform.scale(background_3, (DEFAULT.window_width, DEFAULT.window_height))


Players = pygame.sprite.Group()
player = Player()
Players.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    window.blit(background_r, (0, 0))
    window.blit(background_2_r, (0, 0))
    window.blit(background_3_r, (0, 0))
    Players.draw(window)
    pygame.display.flip()
    pygame.display.update()

    clock.tick(DEFAULT.FPS)

pygame.quit()
