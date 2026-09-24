import numpy as np

class Particle:
    def __init__(self, position, velocity, mass, id, radius):
        self.position = position # np.array
        self.velocity = velocity # np.array
        self.force    = np.zeros(3)
        self.mass     = mass 
        self.id       = id
        self.radius   = radius
        
class n_body_system:
    def __init__(self, particules, dt, softening):
        self.particles = particules
        self.dt        = dt
        self.softening = softening

def init_systeme_Plummer(systeme, nb_particules, M_tot, a, G):
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
            radius   = 1
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
        systeme.particles = np.append(systeme.particles, objet)
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
