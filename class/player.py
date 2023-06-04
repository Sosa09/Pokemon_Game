# Created and managed by Tanguy and Soufiane

from trainer import Trainer
class Player(Trainer):

    def __init__(self, pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.bag = [] #container for potion, pokeballs, pokemons
        self.pokemons = []
        self.battle_x = 1280
        self.battle_y = 380
        self.battleImage = self.pygame.image.load("Images/Trainers/ashBattle.png").convert_alpha()
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
        
        
    # Display Battle elements dynamically (Player )
    def show_trainer(self, pygame, game):
        #load the trainer image
        image = self.battleImage
        image = pygame.transform.scale(image, (100, 100))
        game.screen.blit(image, (self.battle_x, self.battle_y))
        
    def pokemon_choice(self, pygame, game):
        #load the pokemon trainer image
        image = self.pokemons[0].image
        image = pygame.transform.scale(image, (100, 100))
        game.screen.blit(image, (50, 380))
        #health bar pokemon trainer
        pygame.draw.rect(game.screen, "black",(200,400,850,60),5, 1,1,1,1,1)
        pygame.draw.rect(game.screen, "red", (210,410,830,40))  