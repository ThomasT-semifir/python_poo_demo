class Voiture:
    """une voiture.

    Attrs:
        marque (str): marque de la voiture
        ...

    """

    def __init__(self,  marque: str, couleur: str ="blanc" ):
        self.__couleur = couleur
        self._marque = marque

    @property
    def marque(self):
        return self._marque

    @property
    def couleur(self):
        """
            Le décoraeur property permet de définir directement la propriété. Ces un sucre syntaxique qui nous esdt proposé
        """
        return self.__couleur

    @couleur.setter
    def couleur(self, couleur):
        if (type(couleur) is not str):
            raise TypeError("La couleur doit être une chaîne de caractères!")
        self.__couleur = couleur

    # def get_couleur(self):
    #     return self.couleur

    # def set_couleur(self, value):
    #     self.couleur = value

    def __str__(self) -> str:
        return f"La voiture est de marque {self._marque} et de couleur {self._couleur}"

voiture_1 = Voiture("peugeot", "bleu")
voiture_1.couleur = 21212
print(voiture_1.couleur)
