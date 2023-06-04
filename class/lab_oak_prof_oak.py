import pygame

class ProfessorOak(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        test = pygame.image.load('images/Professor/profoak1.png').convert_alpha()
        self.image = pygame.transform.scale(test, (70, 70))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 0)  # changed for collision
        self.name = "Doc. Oak"
