import pygame
import sys
import subprocess

# Initialisation de Pygame
pygame.init()
max_hp = 10
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FONT_SIZE = 32

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
character1_pos = [0, 0]
character2_pos = [0, 0]
character1_hp = 10
character2_hp = 10

# Initialisation de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stickman")

# Charger les polices
base_font = pygame.font.Font(None, FONT_SIZE)
big_font = pygame.font.Font(None, int(FONT_SIZE * 1.1))

# Fonction pour charger les images depuis les fichiers
def load_images():
    background_options = ["assets/images/newfond.webp", "assets/images/autre_fond1.webp", "assets/images/autre_fond2.webp", "assets/images/autre_fond3.webp", "assets/images/autre_fond4.webp"]
    selected_background = select_background_menu(screen)
    background_image = pygame.image.load(selected_background).convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    character1_image = pygame.image.load("assets/images/stickman0g.png").convert_alpha()
    character2_image = pygame.image.load("assets/images/stickman1.png").convert_alpha()
    character1_walk_image = pygame.image.load("assets/images/marche1.png").convert_alpha()
    character2_walk_image = pygame.image.load("assets/images/marche2.png").convert_alpha()

    character1_image = pygame.transform.scale(character1_image, (200, 400))
    character2_image = pygame.transform.scale(character2_image, (200, 400))
    character1_walk_image = pygame.transform.scale(character1_walk_image, (200, 400))
    character2_walk_image = pygame.transform.scale(character2_walk_image, (200, 400))

    character1_attack_image = pygame.image.load("assets/images/stackmand1.png").convert_alpha()
    character2_attack_image = pygame.image.load("assets/images/stackmand2.png").convert_alpha()

    character1_attack_image = pygame.transform.scale(character1_attack_image, (200, 400))
    character2_attack_image = pygame.transform.scale(character2_attack_image, (200, 400))

    return background_image, character1_image, character2_image, character1_walk_image, character2_walk_image, character1_attack_image, character2_attack_image

# Fonction pour afficher le menu de sélection de l'image de fond
def select_background_menu(screen):
    clock = pygame.time.Clock()
    background_options = ["assets/images/newfond.webp", "assets/images/newfond2.webp", "assets/images/newfond3.webp", "assets/images/newfond4.webp", "assets/images/newfond5.webp"]
    selected_option = 0

    running = True
    while running:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(background_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(background_options)
                elif event.key == pygame.K_RETURN:
                    return background_options[selected_option]

        for i, option in enumerate(background_options):
            text_surface = font.render(option, True, (255, 255, 255) if i == selected_option else (100, 100, 100))
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 50))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)

# Fonction pour dessiner la barre de vie au-dessus d'un personnage
def draw_health_bar(screen, character_pos, current_hp, max_hp):
    bar_length = 100
    bar_height = 10
    outline_rect = pygame.Rect(character_pos[0] - 50, character_pos[1] - 20, bar_length, bar_height)
    filled_rect = pygame.Rect(character_pos[0] - 50, character_pos[1] - 20, int(bar_length * (current_hp / max_hp)), bar_height)
    pygame.draw.rect(screen, (255, 255, 255), outline_rect, 2)
    pygame.draw.rect(screen, (0, 255, 0), filled_rect)

# Fonction pour afficher le gagnant et le bouton pour quitter
def display_winner(screen, winner):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Le gagnant est : {winner}", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text_surface, text_rect)

    font = pygame.font.Font(None, 24)
    button_text_surface = font.render("Quitter", True, (255, 255, 255))
    button_rect = button_text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.draw.rect(screen, (0, 0, 255), button_rect)
    screen.blit(button_text_surface, button_rect.topleft)

    pygame.display.flip()  
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    waiting = False

# Fonction pour le menu principal du jeu
def main_menu():
    clock = pygame.time.Clock()
    background_image = pygame.image.load('assets/images/Fonds.jpg').convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    images = load_images()

    button_width = SCREEN_WIDTH // 2
    button_height = FONT_SIZE * 2
    button_margin = 20
    start_y = (SCREEN_HEIGHT - ((button_height * 4) + (button_margin * 3))) // 2

    play_button_rect = pygame.Rect((SCREEN_WIDTH / 4, start_y, button_width, button_height))
    settings_button_rect = pygame.Rect((SCREEN_WIDTH / 4, start_y + button_height + button_margin, button_width, button_height))
    score_button_rect = pygame.Rect((SCREEN_WIDTH / 4, start_y + (button_height + button_margin) * 2, button_width, button_height))
    quit_button_rect = pygame.Rect((SCREEN_WIDTH / 4, start_y + (button_height + button_margin) * 3, button_width, button_height))

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        play_hovered = play_button_rect.collidepoint(mouse_pos)
        settings_hovered = settings_button_rect.collidepoint(mouse_pos)
        score_hovered = score_button_rect.collidepoint(mouse_pos)
        quit_hovered = quit_button_rect.collidepoint(mouse_pos)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    game_loop(screen, images)
                    print("Jouer cliqué")

                elif settings_button_rect.collidepoint(event.pos):
                    subprocess.Popen(["python", "src/settings.py"])
                    print("Paramètres cliqué !")

                elif score_button_rect.collidepoint(event.pos):
                    subprocess.run(["python", "src/Score.py"])
                    print("Score cliqué !")

                elif quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(background_image, (0, 0))

        screen.blit(create_button("Jouer", play_button_rect, RED, play_hovered), play_button_rect.topleft)
        screen.blit(create_button("Paramètres", settings_button_rect, BLUE, settings_hovered), settings_button_rect.topleft)
        screen.blit(create_button("Score", score_button_rect, RED, score_hovered), score_button_rect.topleft)
        screen.blit(create_button("Quitter", quit_button_rect, BLUE, quit_hovered), quit_button_rect.topleft)

        pygame.display.flip()
        clock.tick(60)
        #je ne suis pas 

# Fonction pour créer un bouton avec du texte
def create_button(text, rect, base_color, is_hovered):
    font = big_font if is_hovered else base_font
    color = YELLOW if is_hovered else base_color
    button_surface = pygame.Surface(rect.size)
    button_surface.fill(color)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(rect.width // 2, rect.height // 2))
    button_surface.blit(text_surface, text_rect)
    return button_surface

# Fonction principale pour la boucle de jeu
def game_loop(screen, images):
    background_image, character1_image, character2_image, character1_walk_image, character2_walk_image, character1_attack_image, character2_attack_image = images

    character1_pos = [SCREEN_WIDTH / 3 - 50, SCREEN_HEIGHT / 2 - 100]
    character2_pos = [2 * SCREEN_WIDTH / 3 - 50, SCREEN_HEIGHT / 2 - 100]
    character1_hp = 10
    character2_hp = 10

    running = True
    move_speed = 10
    jump_height = 250
    gravity = 10
    player1_attack_distance = 300
    player2_attack_distance = 300
    damage = 1
    attack_duration = 500

    character1_attacking = False
    character2_attacking = False
    character1_walking = False
    character2_walking = False

    last_attack_time_1 = 0
    last_attack_time_2 = 0
    last_jump_time_1 = 0
    last_jump_time_2 = 0
    jump_cooldown = 1000

    clock = pygame.time.Clock()

    while running:
        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        # Player 1 movement and gravity
        if keys[pygame.K_z]:
            character1_pos[0] += move_speed
            character1_walking = True
        elif keys[pygame.K_s]:
            character1_pos[0] -= move_speed
            character1_walking = True
        else:
            character1_walking = False

        if keys[pygame.K_SPACE] and current_time - last_jump_time_1 > jump_cooldown:
            character1_pos[1] -= jump_height
            last_jump_time_1 = current_time

        # Player 2 movement and gravity
        if keys[pygame.K_UP]:
            character2_pos[0] += move_speed
            character2_walking = True
        elif keys[pygame.K_DOWN]:
            character2_pos[0] -= move_speed
            character2_walking = True
        else:
            character2_walking = False

        if keys[pygame.K_LEFT] and current_time - last_jump_time_2 > jump_cooldown:
            character2_pos[1] -= jump_height
            last_jump_time_2 = current_time

        # Apply gravity
        if character1_pos[1] < SCREEN_HEIGHT / 2 - 100:
            character1_pos[1] += gravity
        if character2_pos[1] < SCREEN_HEIGHT / 2 - 100:
            character2_pos[1] += gravity

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Player 1 attacks with left click if the click is within player 2's attack range
                if event.button == 1:  # Left mouse button
                    if abs(mouse_x - character2_pos[0]) < player1_attack_distance and abs(mouse_y - character2_pos[1]) < player1_attack_distance:
                        if not character1_attacking:  # Check if player 1 is not already attacking
                            character2_hp -= damage
                            character1_attacking = True
                            last_attack_time_1 = current_time
                # Player 2 attacks with right click if the click is within player 1's attack range
                elif event.button == 3:  # Right mouse button
                    if abs(mouse_x - character1_pos[0]) < player2_attack_distance and abs(mouse_y - character1_pos[1]) < player2_attack_distance:
                        if not character2_attacking:  # Check if player 2 is not already attacking
                            character1_hp -= damage
                            character2_attacking = True
                            last_attack_time_2 = current_time

        # Reset attack states after the duration
        if character1_attacking and (current_time - last_attack_time_1 > attack_duration):
            character1_attacking = False
        if character2_attacking and (current_time - last_attack_time_2 > attack_duration):
            character2_attacking = False

        # Draw the scene
        screen.blit(background_image, (0, 0))
        if character1_attacking:
            screen.blit(character1_attack_image, character1_pos)
        elif character1_walking:
            screen.blit(character1_walk_image, character1_pos)
        else:
            screen.blit(character1_image, character1_pos)

        if character2_attacking:
            screen.blit(character2_attack_image, character2_pos)
        elif character2_walking:
            screen.blit(character2_walk_image, character2_pos)
        else:
            screen.blit(character2_image, character2_pos)

        draw_health_bar(screen, character1_pos, character1_hp, max_hp)
        draw_health_bar(screen, character2_pos, character2_hp, max_hp)

        if character1_hp <= 0 or character2_hp <= 0:
            winner = "Player 1" if character2_hp <= 0 else "Player 2"
            display_winner(screen, winner)
            running = False

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main_menu()
