import pygame

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

while game_is_running:

    # Lyt til alle signaler og gem dem i variablen signal.
    for signal in pygame.event.get():
    
        if signal.type == pygame.QUIT:
            quit()
    
    # Hent musens position.
    mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
    
    # Opdater kassens position med musens position.
    box_position_x = mouse_position_x - box_image_back.get_width()/2
    
    # Tegn baggrundsbilledet.
    window.blit(background_image, (0, 0))
    
    # Tegn bagsiden af kassen.
    window.blit(box_image_back, (box_position_x, box_position_y))
    
    # Tegn forsiden af kassen.
    window.blit(box_image_front, (box_position_x, box_position_y + 50))
    
    # Opdater vinduet.
    pygame.display.update()

