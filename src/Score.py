import pygame
import sys
 
# Initialisation de Pygame
pygame.init()
 
# Configuration de la fenêtre
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Score")
 
# Couleurs
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
DEEP_BLUE = (0, 191, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 223, 0)
RED = (255, 69, 0)
 
# Polices
font = pygame.font.Font(None, 32)
title_font = pygame.font.Font(None, 48)  # Police plus grande pour le titre
 
# Données simulées pour les joueurs
players = [
    {"name": "Mirza", "wins": 300, "win_rate": "90.99%", "Pays": "BIH"},
    {"name": "Mathieu", "wins": 257, "win_rate": "87.71%", "Pays": "FR"},
    {"name": "Tsiory", "wins": 290, "win_rate": "100%", "Pays": "MDG"},
    {"name": "Taha", "wins": 270, "win_rate": "70%", "Pays": "TN"},
]
 
# Trier les joueurs par 'wins' en ordre décroissant
players = sorted(players, key=lambda x: x['wins'], reverse=True)
 
def draw_leaderboard():
    screen.fill(DEEP_BLUE)  # Utiliser une couleur de fond vive
    # Dessiner le titre
    title_surface = title_font.render("Classement des Joueurs", True, YELLOW)
    title_rect = title_surface.get_rect(center=(screen_width // 2, 30))
    screen.blit(title_surface, title_rect)
    # Dessiner les en-têtes
    headers = ["Rank", "Name",  "Wins", "Win %", "Pays"]
    header_x_start = 50
    y_offset = 80
    x_offset_increment = 120
 
    for i, header in enumerate(headers):
        text_surface = font.render(header, True, WHITE)
        screen.blit(text_surface, (header_x_start + i * x_offset_increment, y_offset))
 
    # Dessiner les données des joueurs avec des couleurs alternées pour chaque ligne
    for index, player in enumerate(players):
        y = y_offset + 40 * (index + 1)
        background_color = LIGHT_BLUE if index % 2 == 0 else WHITE
        pygame.draw.rect(screen, background_color, pygame.Rect(header_x_start, y, 700, 30))
 
        # Dynamiquement générer le rang basé sur l'index
        rank = index + 1
        player_data = [
            str(rank),
            player['name'],
            str(player['wins']),
            player['win_rate'],
            player['Pays']
        ]
        for j, data in enumerate(player_data):
            text_surface = font.render(data, True, GREEN if headers[j] == 'Wins' else RED)
            screen.blit(text_surface, (header_x_start + j * x_offset_increment, y))
 
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
        draw_leaderboard()
        pygame.display.flip()
 
if __name__ == "__main__":
    main()