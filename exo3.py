class Student:
    
    def __init__(self, nom, note_1, note_2):
        self.__nom = nom
        self.__note_1 = note_1
        self.__note_2 = note_2

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    # ... autres properties ...

    def moyenne(self):
        """
        Calcule la moyenne des notes de l'élève
        """
        return (self.__note_1 + self.__note_2) / 2

