import pygame

class Camera3D:
    def __init__(self, screen_width, screen_height, focal_length=600):
        """Caméra simple pour la projection perspective 3D vers 2D.

        Args:
            screen_width (int): Largeur de l'écran en pixels.
            screen_height (int): Hauteur de l'écran en pixels.
            focal_length (float): Distance focale virtuelle (contrôle l'intensité de la perspective).
        """
        self.center_x = screen_width // 2
        self.center_y = screen_height // 2
        self.focal_length = focal_length

        # Position de la caméra dans l'espace physique
        self.x = 0.0
        self.y = 0.0
        self.z = -1000.0  # Reculée le long de l'axe Z pour observer la scène

def projeter_3d_vers_2d(pos_3d, camera):
    """Projette un point (X, Y, Z) du monde physique vers les coordonnées écran (px, py).

    Returns:
        tuple ou None: (px, py, echelle) si la particule est devant la caméra, None sinon.
    """
    # Position relative de la particule par rapport à la caméra
    rel_x = pos_3d[0] - camera.x
    rel_y = pos_3d[1] - camera.y
    rel_z = pos_3d[2] - camera.z

    # Ignorer/cliper les particules situées derrière ou trop près de l'objectif
    if rel_z <= 1.0:
        return None

    # Facteur de perspective inversement proportionnel à la distance en Z
    echelle = camera.focal_length / rel_z

    # Projection centrale
    px = int(rel_x * echelle + camera.center_x)
    py = int(-rel_y * echelle + camera.center_y)  # Inversion de l'axe Y pour Pygame

    return px, py, echelle

def init_fenetre_rendu(largeur, hauteur, titre="Simulation N-corps", icon=None):
    """Initialise la fenêtre graphique Pygame.

    Args:
        largeur (int): largeur de la fenêtre en pixels
        hauteur (int): hauteur de la fenêtre en pixels
        titre (str, optional): titre de la fenêtre.
        icon (str, optional): chemin vers le fichier image de l'icône.
    """
    pygame.init()
    
    # Conversion explicite en int pour Pygame
    ecran = pygame.display.set_mode((int(largeur), int(hauteur)))
    pygame.display.set_caption(titre)
    
    # On ne charge l'icône que si un chemin a été fourni
    if icon is not None:
        image = pygame.image.load(icon).convert()
        pygame.display.set_icon(image)
        
    return ecran

def afficher_particules_3d(systeme, camera, ecran):
    """Affiche les particules du système avec effet de perspective et gestion de profondeur.

    Args:
        systeme: Objet contenant 'systeme.particles' (liste de particules)
                 Chaque particule possède :
                   - p.position : array-like de taille 3 [x, y, z]
                   - p.radius
        camera (Camera3D): Instance de la caméra
        ecran (pygame.Surface): Surface de rendu Pygame
    """
    # 1. Fond noir (efface le rendu précédent pour éviter toute traînée)
    ecran.fill((0, 0, 0))

    # 2. Tri par profondeur (Axe Z croissant, du plus éloigné au plus proche)
    # L'algorithme du peintre assure que le premier plan recouvre l'arrière-plan
    particules_triees = sorted(
        systeme.particles, key=lambda p: p.position[2], reverse=True
    )

    # 3. Projection et rendu de chaque particule
    for p in particules_triees:
        res = projeter_3d_vers_2d(p.position, camera)
        if res is None:
            continue

        px, py, echelle = res

        # Rayon physique (par défaut à 2.0 si non spécifié sur la particule)
        rayon_physique = p.radius

        # Rayon apparent sur l'écran (dépend de la distance Z)
        rayon_ecran = max(1, int(rayon_physique * echelle))

        # Varier l'intensité lumineuse pour renforcer l'illusion d'éloignement/profondeur
        # Plus Z est grand (éloigné), plus la couleur est assombrie
        attenuation = max(0.2, min(1.0, 1000.0 / (p.position[2] - camera.z)))
        couleur = (
            int(255 * attenuation),
            int(255 * attenuation),
            int(255 * attenuation),
        )

        # Dessin du corps
        pygame.draw.circle(ecran, couleur, (px, py), rayon_ecran)

    # 4. Rafraîchissement du tampon d'affichage
    pygame.display.flip()