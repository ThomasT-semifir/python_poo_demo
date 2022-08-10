from exo5 import Point

class PointFactory:

    @staticmethod
    def creer_point():
        abs = int(input("entrez la valeur de x:"))
        ord = int(input("entrez la valeur de y:"))
        return Point(abs,ord)
        