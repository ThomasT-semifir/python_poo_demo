from exo_7 import Maison


class Appartement(Maison):
    def __init__(self, couleur_porte):
        super().__init__(couleur_porte, 50)