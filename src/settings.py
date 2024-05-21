import pygame
import sys
 
# Initialisation de Pygame
pygame.init()
 
# Configuration de la fenêtre
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Settings")
 
# Couleurs
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
DARK_GREY = (50, 50, 50)
RED = (255, 0, 0)
 
# Polices
font = pygame.font.Font(None, 32)
 
# Textes pour les options (suppression de "Controls")
options = ["Volume", "Resolution"]
values = ["100%", "1920x1080"]
 
# Ajoutez la définition de return_rect en dehors de la fonction draw_settings
return_text = "Return"
return_surface = font.render(return_text, True, WHITE)
return_rect = return_surface.get_rect(center=(screen_width // 2, screen_height - 50))
 
def draw_settings():
    screen.fill(DARK_GREY)
    y_offset = 100
    for i, option in enumerate(options):
        text_surface = font.render(option, True, WHITE)
        value_surface = font.render(values[i], True, GREY)
        text_rect = text_surface.get_rect(x=100, y=y_offset)
        value_rect = value_surface.get_rect(x=400, y=y_offset)
        screen.blit(text_surface, text_rect)
        screen.blit(value_surface, value_rect)
        # Drawing a button for changing settings (placeholder)
        pygame.draw.rect(screen, RED, (600, y_offset, 150, 30), 2)
        y_offset += 50
 
    # Dessiner le bouton "Retour"
    pygame.draw.rect(screen, RED, return_rect.inflate(20, 10))  # Inflate to make the background larger than the text
    screen.blit(return_surface, return_rect)
 
def handle_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifiez si le bouton "Retour" est cliqué
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if return_rect.collidepoint(mouse_x, mouse_y):
                running = False  # Changez running à False pour quitter la boucle
                print("Bouton return cliqué")
 
def main():
    global running
    running = True
    while running:
        handle_events()
        draw_settings()
        pygame.display.flip()
 
if __name__ == "__main__":
    main()
