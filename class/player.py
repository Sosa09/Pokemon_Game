# Created and managed by Tanguy, and partially Soufiane

from trainer import Trainer
class Player(Trainer):

    def __init__(self, pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = self.pygame.image.load('Images/Trainers/ash.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = self.pygame.math.Vector2()
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: #moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: #moving left
                        self.rect.left = sprite.rect.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: #moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: #moving up
                        self.rect.top = sprite.rect.bottom

    def input(self):
        keys = self.pygame.key.get_pressed()
        if keys[self.pygame.K_UP]:
            self.direction.y = -1
        elif keys[self.pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[self.pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[self.pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def update(self):
        self.input()
        self.move(self.speed)

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
        
        
