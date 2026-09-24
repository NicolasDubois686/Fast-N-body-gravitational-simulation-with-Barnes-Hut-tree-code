import numpy as np
import pygame

class Camera2D:
    def __init__(self, target_x=0.0, target_y=0.0, zoom=1.0):
        self.target = np.array([target_x, target_y])  # Le point physique ciblé au centre de l'écran
        self.zoom = zoom                              # Facteur d'agrandissement (ex: 1.0, 2.5, 0.2)
        self.screen_center = np.array([640, 360])     # Milieu de la fenêtre en pixels (1280x720 / 2)

class Camera3D:
    def __init__(self):
        self.position = np.array([0.0, 50.0, 100.0])  # Emplacement de l'œil dans l'espace
        self.target = np.array([0.0, 0.0, 0.0])       # Le point que la caméra regarde (le centre de la galaxie)
        self.up = np.array([0.0, 1.0, 0.0])           # Le vecteur "Haut" pour s'orienter
        self.fov = 45.0                               # Champ de vision en degrés (Field of View)

def init_fenetre(largeur, hauteur, titre = "Simulation N-corps", icon = None):
    """Initialise la fenêtre graphique Pygame

    Args:
        largeur (int): largeur de la fenêtre d'affichage
        hauteur (int): hauteur de la fenêtre d'affichage
        titre   (str): titre de la fenêtre d'affichage
        icon    (str): chemin d'accès vers l'icon de la page, par défaut il n'y en a pas
    """
    pygame.init()
    # dimmensions de la fenêtre (largeur x hauteur)
    ecran = pygame.display.set_mode((largeur, hauteur))
    # titre de la fenêtre
    pygame.display.set_caption(titre)
    # icone de la fenêtre
    if icon is not None :
        image = pygame.image.load(icon).convert()
        pygame.display.set_icon(image)
    # Contrôle de la vitesse d'affichage
    clock = pygame.time.Clock()
    return (ecran, clock)
    
def afficher_particules(systeme, camera):
    """Projecte les coordonnées 3D en 2D des particules 

    Args:
        systeme (n_body_system): état courant du systeme
        camera (_type_): _description_
    """