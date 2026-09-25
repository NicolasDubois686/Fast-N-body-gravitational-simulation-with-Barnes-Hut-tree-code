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
# Définition des constantes #
#############################

LARGEUR = 1580
HAUTEUR = 720
DUREE   = 10000
NB_PARTICLES = 10
SUB_STEPS = 10

a = 10
M_tot = 10

############################
# Initialisation affichage #
############################

camera = Camera3D(
    screen_width  = LARGEUR,
    screen_height = HAUTEUR,
    focal_length  = 5000
)

ecran = init_fenetre_rendu(LARGEUR, HAUTEUR, titre="Simulation N-corps - Plummer 3D")
clock = pygame.time.Clock()

#############################
# Initialisation du système #
#############################

systeme = n_body_system(
    particules = np.array([]),
    dt         = 0.05,
    softening  = 0.5
)

init_systeme_Plummer(systeme, NB_PARTICLES, M_tot, a, G)

#############################
#     N-corps Algorithm     #
#############################

afficher_particules_3d(systeme, camera, ecran)

simulation_active = True
t = 0
while (t < DUREE and simulation_active) :
    for _ in range(SUB_STEPS):
        calculer_toutes_les_forces(systeme)
        mettre_a_jour_position_et_vitesse(systeme)
        t += systeme.dt
    nb_in_screen = afficher_particules_3d(systeme, camera, ecran)
    clock.tick(60)
    if nb_in_screen < 2 * NB_PARTICLES / 3 :
        simulation_active = False
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            simulation_active = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q :
                simulation_active = False

pygame.quit()