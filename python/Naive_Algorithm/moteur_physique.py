import numpy as np

def reinitialiser_forces(systeme): 
    """Remet à zéro les vecteurs forces de chaque corp avant le calcul du pas courant

    Args:
        systeme (n_body_system): état courant du système
    """
    for particule in systeme.particles :
        particule.force = np.zeros(3)
    return 

def calculer_force_paire(particule_A, particule_B, softening):
    """Calcule la force d'attraction gravitationnelle exercée par B sur A (vectoriellement) en appliquant le paramètre d'adoucissement

    Args:
        particule_A (Paticle): état courant de la particule
        particule_B (Particle): état courant de la particule
        softening (float): parametre d'adoucissement gravitationnel
    """
    return

def calculer_toutes_les_forces(systeme):
    """Double boucle imbriquée qui parcourt toutes les paires distinctes (i,j) pour faire la somme des forces subies par chaque particule

    Args:
        systeme (n_body_system): état courant du système
    """
    return 