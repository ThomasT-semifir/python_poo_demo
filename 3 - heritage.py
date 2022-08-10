class Vehicule(object):
    def __init__(self, couleur):
        super().__init__()
        self._couleur = couleur

    @property
    def couleur(self):
        return self._couleur
    
    @couleur.setter
    def couleur(self, value):
        self._couleur = value

    def se_deplacer(self):
        return "Je me déplace"

class Voiture(Vehicule):

    nb_roues: 4

    def __init__(self, couleur, marque):
        super().__init__(couleur)
        self.__marque = marque

    def _accelerer(self):
        return "J'accélère"

    def appuyer_accelerateur(self):
        return self._accelerer()

    def se_deplacer(self):
        return f"{self.appuyer_accelerateur()} : {super().se_deplacer()}"

voiture = Voiture("bleue", "udkhtrjf")
print(voiture._couleur)
print(voiture.se_deplacer())


class Camionnette(Voiture):
    def __init__(self, couleur, marque, charge_max):
        super().__init__(couleur, marque)
        self._charge_max = charge_max

    @property
    def charge_max(self):
        return self._charge_max

    @charge_max.setter
    def charge_max(self, value):
        self._charge_max = value

class Moto(Vehicule):
    nb_roues: 2

    def __init__(self, couleur, type):
        super().__init__(couleur)
        self.__type = type

    def _accelerer(self):
        return "vroum"

    def tourner_poignee_gaz(self):
        return self._accelerer()

    def se_deplacer(self):
        return f"{self.tourner_poignee_gaz()} : {super().se_deplacer()}"

moto = Moto("rouge", "roadster")
print(moto.se_deplacer())