import pygame

class ProfessorOak(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.sprite_image = pygame.image.load('images/Professor/profoak1.png')
        if self.sprite_image.get_alpha() is None:
            self.sprite_image = self.sprite_image.convert()  # Convert the image to include an alpha channel
        else:
            self.sprite_image = self.sprite_image.convert_alpha()
        self.scaled_sprite_image = pygame.transform.smoothscale(self.sprite_image, (70, 60))
        self.rect = self.scaled_sprite_image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 0)  # changed for collision
        self.name = "Doc. Oak"
