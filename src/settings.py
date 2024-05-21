import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
largeur_ecran, hauteur_ecran = 800, 600
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Paramètres")

# Couleurs
BLANC = (255, 255, 255)
GRIS_CLAIR = (200, 200, 200)
GRIS_FONCE = (50, 50, 50)
ROUGE = (255, 0, 0)

# Polices
police = pygame.font.Font(None, 32)

# Textes pour les options (ajout de "Musique")
options = ["Volume", "Résolution", "Musique"]
valeurs = ["100%", "1920x1080", "Musique sélectionnée: Aucune"]
musique_selectionnee = None  # Variable pour stocker la musique sélectionnée

# Liste des musiques disponibles
options_musique = ["Musique 1"]
zone_selection_musique = pygame.Rect(600, 200, 150, 30)
liste_musique_etendue = False

# Définition de retour_rect en dehors de la fonction draw_settings
texte_retour = "Retour"
surface_retour = police.render(texte_retour, True, BLANC)
retour_rect = surface_retour.get_rect(center=(largeur_ecran // 2, hauteur_ecran - 50))

def dessiner_parametres():
    ecran.fill(GRIS_FONCE)
    y_offset = 100
    for i, option in enumerate(options):
        surface_texte = police.render(option, True, BLANC)
        if option == "Musique":
            surface_valeur = police.render(musique_selectionnee if musique_selectionnee else "Aucune", True, GRIS_CLAIR)
            pygame.draw.rect(ecran, ROUGE, zone_selection_musique, 2)
            if liste_musique_etendue:
                for idx, musique in enumerate(options_musique):
                    surface_musique = police.render(musique, True, GRIS_CLAIR)
                    zone_musique = surface_musique.get_rect(x=600, y=200 + 30 * (idx + 1))
                    pygame.draw.rect(ecran, GRIS_FONCE, zone_musique)
                    ecran.blit(surface_musique, zone_musique)
        else:
            surface_valeur = police.render(valeurs[i], True, GRIS_CLAIR)
            if i < 2:  # Dessiner une case rouge à droite des options "Volume" et "Résolution"
                pygame.draw.rect(ecran, ROUGE, (600, y_offset, 150, 30), 2)
        zone_texte = surface_texte.get_rect(x=100, y=y_offset)
        zone_valeur = surface_valeur.get_rect(x=400, y=y_offset)
        ecran.blit(surface_texte, zone_texte)
        ecran.blit(surface_valeur, zone_valeur)
        y_offset += 50

    # Dessiner le bouton "Retour"
    pygame.draw.rect(ecran, ROUGE, retour_rect.inflate(20, 10))
    ecran.blit(surface_retour, retour_rect)

def gerer_evenements():
    global en_cours, musique_selectionnee, liste_musique_etendue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if retour_rect.collidepoint(mouse_x, mouse_y):
                en_cours = False
                print("Bouton retour cliqué")
            elif zone_selection_musique.collidepoint(mouse_x, mouse_y):
                liste_musique_etendue = not liste_musique_etendue
            elif liste_musique_etendue:
                for idx, musique in enumerate(options_musique):
                    zone_musique = pygame.Rect(600, 200 + 30 * (idx + 1), 150, 30)
                    if zone_musique.collidepoint(mouse_x, mouse_y):
                        musique_selectionnee = musique
                        liste_musique_etendue = False
                        print("Musique sélectionnée:", musique_selectionnee)
                        # Lire la musique sélectionnée
                        pygame.mixer.music.load("assets/sounds/Inst.mp3")
                        pygame.mixer.music.play()

def principal():
    global en_cours
    en_cours = True
    while en_cours:
        gerer_evenements()
        dessiner_parametres()
        pygame.display.flip()

if __name__ == "__main__":
    principal()
