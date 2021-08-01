import pygame
from random import randint

# Start pygame og alle dens moduler
pygame.init()
pygame.font.init()

# Opret et vindue med en opløsning på 800x600 pixels.
window_width = 800
window_height = 600
window_title = "Mit Første Spil!"
resolution = (window_width, window_height)
game_is_running = True

pygame.display.set_caption(window_title)
window = pygame.display.set_mode(resolution)

# indlæs baggrundsbilledet.
background_image = pygame.image.load("graphics/background.png").convert()

# Indlæs kassen som spilleren skal styre.
box_image_back = pygame.image.load("graphics/back_box.png").convert_alpha()
box_image_front = pygame.image.load("graphics/front_box.png").convert_alpha()
box_position_x = 300
box_position_y = window_height - box_image_back.get_height() - 40

# Indlæs flasken som spilleren skal gribe.
bottle_image = pygame.image.load("graphics/bottle.png").convert_alpha()
bottle_position_x = 400
bottle_position_y = 200
bottle_fall_speed = 500

player_score = 0
player_lives = 3

font = pygame.font.Font("graphics/font.otf", 24)

game_over = False

past_time = pygame.time.get_ticks()

# Start spillets game loop.
while game_is_running:

    current_time = pygame.time.get_ticks()
    delta_time = (current_time - past_time) / 1000
    past_time = current_time

    # Lyt til alle signaler og gem dem i variablen signal.
    for signal in pygame.event.get():

        # Luk spillet når luk signalet er modtaget.
        if signal.type == pygame.QUIT:
            quit()

    if not game_over:

        if player_lives == 0:
            game_over = True

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

            player_lives -= 1

        # Opret en rektangle til kassen og flasken.
        box_rectangle = pygame.Rect(box_position_x, box_position_y + 140, box_image_back.get_width(), box_image_back.get_height() - 140)
        bottle_rectangle = pygame.Rect(bottle_position_x, bottle_position_y, bottle_image.get_width(), bottle_image.get_height())

        # Check om kassen på noget tidspunkt rammer flasken.
        if box_rectangle.colliderect(bottle_rectangle):

            bottle_position_y = -bottle_image.get_height()

            bottle_position_x = randint(0, window_width - bottle_image.get_width())

            player_score += 1
            bottle_fall_speed += 50

        # Tegn baggrundsbilledet.
        window.blit(background_image, (0, 0))

        # Tegn bagsiden af kassen.
        window.blit(box_image_back, (box_position_x, box_position_y))

        # Tegn flasken.
        window.blit(bottle_image, (bottle_position_x, bottle_position_y))

        # Tegn forsiden af kassen.
        window.blit(box_image_front, (box_position_x, box_position_y + 50))

        # Skriv hvor mange points spilleren har.
        score_text = font.render(f"Score: { player_score }", True, (0, 0, 0))
        window.blit(score_text, (10, 10))

        live_text = font.render(f"Lives: { player_lives }", True, (0, 0, 0))
        window.blit(live_text, (10, 50))

    else:

        window.fill((0, 0, 0))

        game_over_text = font.render("Game Over!", True, (255, 0, 0))

        center_x = window_width/2 - game_over_text.get_width()/2
        center_y = window_height/2 - game_over_text.get_height()/2

        window.blit(game_over_text, (center_x, center_y))

        final_score_text = font.render(f"You got { player_score } bottles!", True, (255, 255, 255))

        center_x = window_width/2 - final_score_text.get_width()/2

        window.blit(final_score_text, (center_x, center_y + 30))

        left_click, middle_click, right_click = pygame.mouse.get_pressed()

        if left_click:
            player_score = 0
            player_lives = 3

            bottle_fall_speed = 500

            game_over = False

    # Opdater vinduet.
    pygame.display.update()
