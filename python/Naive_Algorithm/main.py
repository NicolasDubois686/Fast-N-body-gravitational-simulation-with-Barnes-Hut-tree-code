import numpy as np
from initialisation import *
from affichage import *
from moteur_physique import *
from integrateur_numerique import *

"""
Structure des données Particules 
   - position : Vecteur3D (x, y, z)
   - vitesse  : Vecteur3D (vx; vy, vz)
   - force    : Vecteur3D (fx, fy, fz)
   - masse    : float
   - id       : int

Structure des Corps : 
    - particules        : Tableau de particules
    - nb_particules     : int
    - dt (pas de temps) : float
    - softening         : float (parametre d'adoucissement gravitationnel)


"""
        
#############################
# Initialisation du système #
#############################

systeme = n_body_system(
    particules = np.array([]),
    dt         = 0.1,
    softening  = 0.1
)

LARGEUR = 1280
HAUTEUR = 720
DUREE   = 1000
NB_PARTICLES = 15

camera = Camera3D(
    screen_width  = LARGEUR,
    screen_height = HAUTEUR,
    focal_length  = 600
)

ecran = init_fenetre_rendu(LARGEUR, HAUTEUR, titre="Simulation N-corps - Plummer 3D")
clock = pygame.time.Clock()

init_systeme_Plummer(systeme, NB_PARTICLES, 3, 1, G)

afficher_particules_3d(systeme, camera, ecran)

t = 0
while t < DUREE :
    calculer_toutes_les_forces(systeme)
    mettre_a_jour_position_et_vitesse(systeme)
    afficher_particules_3d(systeme, camera, ecran)
    t += systeme.dt

pygame.quit()