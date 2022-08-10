class Person:
    def __init__(self, nom):
        self.nom = nom
    
    def __str__(self):
        return self.nom

class Maison:

    

    def __init__(self, couleur, proprio):
        
        self.couleur = couleur
        self.proprio = proprio

proprio = Person("Thomas")
maison = Maison("rose", proprio)
print(maison.proprio)