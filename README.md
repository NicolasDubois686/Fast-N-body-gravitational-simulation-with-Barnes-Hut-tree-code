# Fast N-body gravitational simulation with Barnes Hut tree code
## Python
### Naive algorithm
Mise en place d'un algorithme naif qui calcul chaque intéraction individuellement et en déduit grace au principe fondamental de la dynamique la position suivante de chaque particule.
#### Structure
Séparation des fonctions dans différents fichiers selon leur utilisation :
1. `initialisation.py` contient les fonctions qui permettent d'initialiser le système (position, vitesse, masse... des particules). \
Utilisation du modèle de Plummer, aussi appelé sphères de Plummer. Il permet de créer un profil de densité spériquement symétrique et isotrope. Il est couramment utilisé en Astrophysique.\
Il offre l'avantage d'être simple à implémenter, avec un coeur de densité uniforme, qui décroit selon une loi de puissance de la forme $$\rho(r) = \frac{3M}{4 \pi a^3}\big(1+(\frac r {u n})^2\big)^{-5/2}$$ avec $M$ la masse totale du système, $r$ la distance radiale à partir du centre, et $u n$ appelé rayon de Plummer qui caractérise la taille du noyau dense. \
La densité centrale est constante sans qu'il n'y ait de singularité : $\rho(0) = \frac{3M}{4 \pi a^3}$. Elle a aussi un comportement asymptotique de $\rho(r)\propto r^{-5}$ qui impose une disparition rapide du noyau.
2. `moteur_physique.py` applique le principe fondamental de la physique (et le principe des actions réciproques) à l'ensemble du système.
3. `integrateur_numerique.py` intègre directement l'accélération calculée par le principe fondamental pour obtenir la position suivante.
4. `affichage.py` utilise le module pygame pour projeter le modèle 3D en 2D et l'afficher dans une fenêtre.
5. `main.py` utilise tous ces fichiers pour simuler le problème à N corps.

#### Complexité & Performances
##### Compléxité temporelle
##### Complexité spatiale

### Barnes Hut algorithm

## Sources
https://idl.uw.edu/living-papers-paper/barnes-hut/ \
https://www.cs.princeton.edu/courses/archive/fall03/cs126/assignments/barnes-hut.html \
https://people.engr.tamu.edu/sueda/courses/CSCE489/2020F/projects/Liam_Bessell/index.html \
https://dev.realworldocaml.org/ \
https://en.wikipedia.org/wiki/Plummer_model \
https://patterns.eecs.berkeley.edu/?page_id=193 