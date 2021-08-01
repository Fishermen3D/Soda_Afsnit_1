import pygame
from random import randint

pygame.init()

# Opret et vindue med en opløsning på 800x600 pixels.
window_width = 800
window_height = 600
window_title = "Mit Første Spil!"
resolution = (window_width, window_height)
game_is_running = True

pygame.display.set_caption(window_title)
window = pygame.display.set_mode(resolution)

# Indlæs baggrundsbilledet.
background_image = pygame.image.load("graphics/background.png").convert()

# Indlæs kassen som spilleren skal styre.
box_image_back = pygame.image.load("graphics/back_box.png").convert_alpha()
box_image_front = pygame.image.load("graphics/front_box.png").convert_alpha()
box_position_x = 200
box_position_y = window_height - box_image_back.get_height() - 40

# Indlæs falsken som spilleren skal gribe.
bottle_image = pygame.image.load("graphics/bottle.png").convert_alpha()
bottle_position_x = 400
bottle_position_y = 200
bottle_fall_speed = 500

past_time = pygame.time.get_ticks()

while game_is_running:

    current_time = pygame.time.get_ticks()
    delta_time = (current_time - past_time) / 1000
    past_time = current_time

    # Lyt til alle signaler og gem dem i variablen signal.
    for signal in pygame.event.get():
    
        if signal.type == pygame.QUIT:
            quit()
    
    # Hent musens position.
    mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
    
    # Opdater kassens position med musens position.
    box_position_x = mouse_position_x - box_image_back.get_width()/2
    
    # Opdater flaskens position.
    bottle_position_y += bottle_fall_speed * delta_time
    
    # Tjek om flasken rammer bunden.
    if bottle_position_y > window_height:
        bottle_position_y = -bottle_image.get_height()
        
        bottle_position_x = randint(0, window_width - bottle_image.get_width())
    
    # Tegn baggrundsbilledet.
    window.blit(background_image, (0, 0))
    
    # Tegn bagsiden af kassen.
    window.blit(box_image_back, (box_position_x, box_position_y))
    
    # Tegn flasken.
    window.blit(bottle_image, (bottle_position_x, bottle_position_y))
    
    # Tegn forsiden af kassen.
    window.blit(box_image_front, (box_position_x, box_position_y + 50))
    
    # Opdater vinduet.
    pygame.display.update()

