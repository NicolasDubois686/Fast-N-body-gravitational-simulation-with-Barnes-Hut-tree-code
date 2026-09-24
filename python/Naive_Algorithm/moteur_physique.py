import numpy as np

global G
G = 3.667 # Constante gravitationnelle

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
    # Vecteur AB
    r_ab = particule_B.position - particule_A.position
    # Norme de la force
    facteur_force = G * particule_A.mass * particule_B.mass / ((np.sqrt(np.sum(r_ab)**2 + softening**2))**3)
    # Force gravitationnelle
    force = facteur_force * r_ab
    return force

def calculer_toutes_les_forces(systeme):
    """Double boucle imbriquée qui parcourt toutes les paires distinctes (i,j) pour faire la somme des forces subies par chaque particule

    Args:
        systeme (n_body_system): état courant du système
    """
    # Remise à 0 des forces subies
    reinitialiser_forces(systeme)
    
    n = len (systeme.particles)
    for i in range(n) : 
        objet_i = systeme.particles[i]
        for j in range(i+1, n) :
            objet_j = systeme.particles[j]
            F_ij = calculer_force_paire(objet_i, objet_j, systeme.softening)
            objet_i.force += F_ij
            objet_j.force += -F_ij
            
    return 