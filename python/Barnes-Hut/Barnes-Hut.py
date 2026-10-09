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

def is_in_node(node, particle):
    """Indique si particle est dans node"""
    return

def cut_node(node):
    """Coupe le noeud en 8 noeud fils de tailles égales"""
      
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