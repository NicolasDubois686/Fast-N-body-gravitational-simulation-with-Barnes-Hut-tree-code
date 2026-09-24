import numpy as np
from main import n_body_system, Particle


def init_systeme_Plummer(systeme, nb_particules, M_tot, a, G, dt, softening):
    """Alloue la mémoire nécessaire pour le tableau de particules avec la méthode de Plummer et définit les constantes physiques globales 

    Args:
        systeme (n_body_systeme): systeme étudié
        nb_particules (int): nombre de corps
        M_tot (float): Masse totale du système
        a (float): rayon d'echelle de Plummer
        G (float): constante gravitationnelle
        dt (float): pas de temps
        softening (float): parametre d'adoucissement gravitationnel
    """
    
    masse_particule = M_tot / nb_particules
    
    for i in range(nb_particules):
        objet = Particle(
            position = np.zeros(3),
            velocity = np.zeros(3),
            mass     = masse_particule,
            id       = i,
            a        = 1
        )
        # génération de la position (r, theta, phi)
        u1 = np.random.uniform(0, 1)
        r = a / np.sqrt(u1 ** (-2/3) - 1)
        
        # Orientation spatiale isotrope
        theta = np.arccos(2 * np.random.uniform(0, 1) - 1)
        phi = 2 * np.pi * np.random.uniform(0, 1)
        
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)
        
        # génération de la vitesse
        v = np.sqrt(2 * G * M_tot / np.sqrt(r**2 + a**2))
        
        # Méthode de rejet pour trouver le facteur q = v / v_e
        q = np.random.uniform(0, 1)
        g = q**2 * (1 - q**2)**3.5
        test = np.random.uniform(0, 0.1)
        while test >= g :
            q = np.random.uniform(0, 1)
            g = q**2 * (1 - q**2)**3.5
            test = np.random.uniform(0, 0.1)
        
        norme_v = q * v
        
        # Orientation de la vitesse isotrope
        theta_v = np.arccos(2 * np.random.uniform(0, 1) - 1)
        phi_v = 2 * np.pi * np.random.uniform(0, 1)
        
        vx = norme_v * np.sin(theta_v) * np.cos(phi_v)
        vy = norme_v * np.sin(theta_v) * np.sin(phi_v)
        vz = norme_v * np.cos(theta_v)
        
        # Stockage dans la particule
        objet.position = np.array([x, y, z])
        objet.velocity = np.array([vx, vy, vz])
        
        # Ajout au systeme
        systeme.particles.append(objet)
    return

def init_systeme_Kuzmin(nb_particules, dt, sftening):
    """Alloue la mémoire nécessaire pour le tableau de particules avec la méthode de Kuzmin et définit les constantes physiques globales

    Args:
        nb_particules (int): nombre de corps
        dt (float): pas de temps
        sftening (float): parametre d'adoucissement gravitationnel
    """
    return

def init_systeme_Navarro_Frenk_White(nb_particules, dt, sftening):
    """Alloue la mémoire nécessaire pour le tableau de particules avec la méthode de Navarro-Frenk-White et définit les constantes physiques globales

    Args:
        nb_particules (int): nombre de corps
        dt (float): pas de temps
        sftening (float): parametre d'adoucissement gravitationnel
    """
    return

def generer_disque_plummer(system, rayon_galaxie, masse_totale):
    """Initialise les positions et les vitesses des corps selon une distribution de Plummer ou un disque en rotation képlérienne (pour obtenir une galaxie stable)

    Args:
        system (n_body_system): état courant du système
        rayon_galaxie (float): 
        masse_totale (float): 
    """
    return