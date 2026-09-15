import numpy as np

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

class Particle:
    def __init__(self, position, velocity, mass):
        self.position = position # np.array
        self.velocity = velocity # np.array
        self.force    = np.zeros(3)
        self.mass     = mass 
        
class n_body_system:
    def __init__(self, particules, dt, softening):
        self.particles = particules
        self.dt        = dt
        self.softening = softening
        
