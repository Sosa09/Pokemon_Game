import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
window_width = 800
window_height = 600
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame Game")

# Load the background image
background_image = pygame.image.load("files_joris\images\oak.jpg")

# Scale the background image to fit the game screen
background_image = pygame.transform.scale(background_image, (800, 600))

# Load the player character image
player_image = pygame.image.load("images/player.png")

# Get the dimensions of the player image
player_width = player_image.get_width()
player_height = player_image.get_height()

# Set the initial position of the player
player_x = (window_width - player_width) // 2
player_y = (window_height - player_height) 

# Set the speed of the player movement
player_speed = 0.5

# Create a separate surface for the background
background_surface = pygame.Surface(window_size)
background_surface.blit(background_image, (0, 0))

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Update the game display
    window.blit(background_surface, (0, 0))
    window.blit(player_image, (player_x, player_y))
    pygame.display.update()

# Quit the game
pygame.quit()
