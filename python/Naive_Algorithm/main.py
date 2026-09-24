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
    dt         = 0.05,
    softening  = 0.5
)

LARGEUR = 1780
HAUTEUR = 720
DUREE   = 10000
NB_PARTICLES = 3
SUB_STEPS = 10

camera = Camera3D(
    screen_width  = LARGEUR,
    screen_height = HAUTEUR,
    focal_length  = 5000
)

ecran = init_fenetre_rendu(LARGEUR, HAUTEUR, titre="Simulation N-corps - Plummer 3D")
clock = pygame.time.Clock()

init_systeme_Plummer(systeme, NB_PARTICLES, 3, 5, G)

afficher_particules_3d(systeme, camera, ecran)

t = 0
while t < DUREE :
    for _ in range(SUB_STEPS):
        calculer_toutes_les_forces(systeme)
        mettre_a_jour_position_et_vitesse(systeme)
        t += systeme.dt
    afficher_particules_3d(systeme, camera, ecran)
    clock.tick(60)

pygame.quit()