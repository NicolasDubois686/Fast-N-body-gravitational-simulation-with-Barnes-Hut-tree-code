import numpy as np

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

def init_fenetre_rendu(largeur, hauteur):
    """Initialise la fenêtre graphique Pygame/VisPy

    Args:
        largeur (float): largeur de la fenêtre d'affichage
        hauteur (float): hauteur de la fenêtre d'affichage
    """
    
def afficher_particules(systeme, camera):
    """Projecte les coordonnées 3D en 2D des particules 

    Args:
        systeme (n_body_system): état courant du systeme
        camera (_type_): _description_
    """