from exo_7 import Porte


class Maison:
    __determinant = "une"
    def __init__(self, couleur_porte, surface):
        self.__porte = Porte(couleur_porte)
        self.__surface = surface
        
    @property
    def porte(self):
        return self.__porte
    
    @porte.setter
    def porte(self, nouvelle_couleur):
        self.__porte = Porte(nouvelle_couleur)
        
    @property
    def surface(self):
        return self.__surface
    
    @surface.setter
    def surface(self, valeur):
        self.__surface = valeur
    
    def presenter_caracteristiques(self):
        return f"Je suis {self.__determinant} {type(self).__name__}, ma surface est de {self.surface} m2 et ma porte va se présenter d'elle-même: {self.porte.presenter_caracteristiques()}"
    