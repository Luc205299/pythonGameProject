import pygame
import DEFAULT


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.animation = [
                            pygame.transform.scale(pygame.image.load(DEFAULT.player_normal), (50,50)) ,
                           pygame.transform.scale(pygame.image.load(DEFAULT.player_jump1), (50, 50)),
                           pygame.transform.scale(pygame.image.load(DEFAULT.player_jump2), (50, 50)),
                           pygame.transform.scale(pygame.image.load(DEFAULT.player_jump3), (50, 50)),
                           pygame.transform.scale(pygame.image.load(DEFAULT.player_jump4), (50, 50)),
                           pygame.transform.scale(pygame.image.load(DEFAULT.player_jump5), (50, 50)),
                           pygame.transform.scale(pygame.image.load(DEFAULT.player_jump6), (50, 50)),
                           pygame.transform.scale(pygame.image.load(DEFAULT.player_jump7), (50, 50))
                           ]

        self.animation_r = [
            pygame.transform.scale(pygame.image.load(DEFAULT.player_normal_r), (50, 50)),
            pygame.transform.scale(pygame.image.load(DEFAULT.player_jump1_r), (50, 50)),
            pygame.transform.scale(pygame.image.load(DEFAULT.player_jump2_r), (50, 50)),
            pygame.transform.scale(pygame.image.load(DEFAULT.player_jump3_r), (50, 50)),
            pygame.transform.scale(pygame.image.load(DEFAULT.player_jump4_r), (50, 50)),
            pygame.transform.scale(pygame.image.load(DEFAULT.player_jump5_r), (50, 50)),
            pygame.transform.scale(pygame.image.load(DEFAULT.player_jump6_r), (50, 50)),
            pygame.transform.scale(pygame.image.load(DEFAULT.player_jump7_r), (50, 50))
        ]

        self.current_frame = 0
        self.frame_count = len(self.animation)
        self.image = self.animation[self.current_frame]




        self.image_x = 100
        self.image_y = 100

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.image_x, self.image_y)



    def update(self):
        keys = pygame.key.get_pressed()
        velocity = 5
        if keys[pygame.K_z]:
            self.rect.y -= velocity
            print("z")
            # Passez à l'image suivante de l'animation
            self.current_frame = (self.current_frame + 1) % self.frame_count

            # Définir l'image actuelle
            self.image = self.animation[self.current_frame]

            # Mettez à jour la position de l'image
            #self.rect.topleft = (self.image_x, self.image_y)

        if keys[pygame.K_s]:
            self.rect.y += velocity
            print("s")
            # Passez à l'image suivante de l'animation
            self.current_frame = (self.current_frame + 1) % self.frame_count

            # Définir l'image actuelle
            self.image = self.animation[self.current_frame]

            # Mettez à jour la position de l'image
            #self.rect.topleft = (self.image_x, self.image_y)

        if keys[pygame.K_q]:
           self.rect.x -= velocity
           # Passez à l'image suivante de l'animation
           self.current_frame = (self.current_frame + 1) % self.frame_count

           # Définir l'image actuelle
           self.image = self.animation[self.current_frame]

           # Mettez à jour la position de l'image
           #self.rect.topleft = (self.image_x, self.image_y)

        if keys[pygame.K_d]:
            self.rect.x += velocity
            # Passez à l'image suivante de l'animation
            self.current_frame = (self.current_frame + 1) % self.frame_count

            # Définir l'image actuelle
            self.image = self.animation[self.current_frame]

            # Mettez à jour la position de l'image
            #self.rect.topleft = (self.image_x, self.image_y)


