class Rectangle:
    
    def __init__(self, longueur: int, largeur:int):
        self.longueur = longueur
        self.largeur = largeur

    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self, value):
        self._longueur = value

    @property
    def largeur(self):
        return self._largeur
    
    @largeur.setter
    def largeur(self, value):
        self._largeur = value

    def surface(self):
        return self._largeur * self._longueur

    def show_mem(self):
        print(self)
