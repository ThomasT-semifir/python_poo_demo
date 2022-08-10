from exo_7 import Maison


class Personne:
    def __init__(self, nom, logement: Maison):
        self.__nom = nom
        self.__logement = logement
        
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value
        
    @property
    def logement(self):
        return self.__logement
    
    @logement.setter
    def logement(self, value):
        self.__logement = value
        
    def presenter_caracteristiques(self):
        return(f"Je m'appelle {self.nom}. {self.logement.presenter_caracteristiques()}")