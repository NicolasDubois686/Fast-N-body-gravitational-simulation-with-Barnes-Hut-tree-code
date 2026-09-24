import numpy as np

def mettre_a_jour_position_et_vitesse(systeme):
    """Met à jour les positions et vitesses de chaque particule à partir de la force accumulée F, en utilisant l'algorithme Leapfrog

    Args:
        systeme (n_body_system): état courant du système
    """
    # Pas de temps
    dt = systeme.dt
    # Calcul de la position suivante d'une particule
    def position_suivante_un_objet(particule, dt):
        # Calcul des positions suivantes
        acceleration = particule.force / particule.mass
        # Calcul des vitesses suivantes
        particule.velocity += acceleration * dt
        # Modification des données
        particule.position += particule.velocity * dt
        # Application à chaque particule
    for particule in systeme.particles :
        position_suivante_un_objet(particule, dt)
    return