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
        x_next = particule.position[0] + particule.velocity[0] * dt + (1/2) * particule.force[0] * (dt**2)
        y_next = particule.position[1] + particule.velocity[1] * dt + (1/2) * particule.force[1] * (dt**2)
        z_next = particule.position[2] + particule.velocity[2] * dt + (1/2) * particule.force[2] * (dt**2)
        # Calcul des vitesses suivantes
        vx_next = (x_next - particule.position[0]) / dt
        vy_next = (y_next - particule.position[1]) / dt
        vz_next = (z_next - particule.position[2]) / dt
        # Modification des données
        particule.position = np.array([x_next, y_next, z_next])
        particule.velocity = np.array([vx_next, vy_next, vz_next])
    # Application à chaque particule
    for particule in systeme.particles :
        position_suivante_un_objet(particule, dt)
    return