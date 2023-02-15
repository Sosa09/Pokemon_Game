import pygame, pokemon, start, map, battle, trainer

pygame.init()
screen = pygame.display.set_mode((800, 600))

#define trainer x, y (load image of trainer later) start position
trainer_x = 50
trainer_y = 50

#set running game to true until quiting the game
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()