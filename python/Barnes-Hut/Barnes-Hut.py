import numpy as np
from initialisation import Particle

class Node:
    
    def __init__(self, center, size):
        self.center   = center
        self.size     = size
        self.mass     = 0.0
        self.com      = np.zeros(3)
        self.state    = 1                           # 1 si feuille 0 sinon
        self.particle = None
        self.children = [None for _ in range(8)]
        
################################
# Construction de l'algorithme #
################################

def mesure_Bounding_Box(node):
    """Indique les coordonnées des angles du cube formé par le noeur `Node`"""
            
    # Coordonnées des angles du cube du noeud
    min_x = node.center[0] - Node.size/2
    min_y = node.center[1] - Node.size/2
    min_z = node.center[2] - Node.size/2
    max_x = node.center[0] + Node.size/2
    max_y = node.center[1] + Node.size/2
    max_z = node.center[2] + Node.size/2
    
    return min_x, max_x, min_y, max_y, min_z, max_z

def is_in_node(node, particle):
    """Indique si particle est dans node"""
    
    # Récupération des coordonnées du cube
    min_x, max_x, min_y, max_y, min_z, max_z = mesure_Bounding_Box(node)
    
    # Vérification
    return ((min_x <= particle.position[0] <= max_x) and
            (min_y <= particle.position[1] <= max_y) and
            (min_z <= particle.position[2] <= max_z))

def cut_node(node):
    """Coupe le noeud en 8 noeud fils de tailles égales"""
    
    # Il faut que le cube ne soit pas encore scindé
    assert(node.children == [None for _ in range(8)])
    
    new_size = node.size / 2
    i = 0
    for x in [1, -1]:
        for y in [1, -1]:
            for z in [1, -1]:
                new_node = Node(
                    center = [node.center[0] + x*new_size/2,
                              node.center[1] + y*new_size/2,
                              node.center[2] + z*new_size/2],
                    size   = new_size
                )
                node.children[i] = new_node
                i += 1
      
def make_tree(node, system):
    """créer l'arbre des particules avec un algorithme de récursivité"""
    
    # Récupération des données des particules
    l_particles = system.particules
    
    def rec(node, particle):
        """fonction recursive qui s'appellera elle même pour positionner la particule"""
        assert is_in_node(node, particle)
        
        # Le noeud n'est pas une feuille
        if node.state == 0 :
            for child in node.children :
                if is_in_node(child, particle) :
                    rec(node, particle)
        # Le noeud est une feuille vide 
        elif (node.particle == None and node.state == 1):
            node.particle = particle
        # Le noeud est une feuille déjà occupée
        elif (node.particle != None and node.state == 1):
            ele = node.particle
            node.particle = None
            node.state = 0
            cut_node()
            for child in node.children :
                if is_in_node(child, ele) :
                    rec(node, ele)
            for child in node.children :
                if is_in_node(child, particle) :
                    rec(node, particle)
        
        return    
    
    return