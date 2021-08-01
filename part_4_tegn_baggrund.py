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

while game_is_running:

    # Lyt til alle signaler og gem dem i variablen signal.
    for signal in pygame.event.get():
    
        if signal.type == pygame.QUIT:
            quit()
    
    # Tegn baggrundsbilledet.
    window.blit(background_image, (0, 0))
    
    # Opdater vinduet.
    pygame.display.update()

