class Porte:
    def __init__(self, couleur):
        self.__couleur = couleur
        
    @property
    def couleur(self):
        return self.__couleur
    
    @couleur.setter
    def couleur(self, valeur):
        self.__couleur = valeur
        
    def presenter_caracteristiques(self):
        return f"Je suis une porte, ma couleur est {self.couleur}"
    