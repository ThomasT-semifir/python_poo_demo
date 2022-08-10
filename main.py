from re import S
from exo1 import Rectangle
from exo2 import Somme
# from exo3 import Student
# from exo4 import Complex
from exo5 import Point
from exo_6 import teacher
from exo_6 import Student, Teacher, Person
from exo_7.maison import Maison
from exo_7.personne import Personne
from pointFactory import PointFactory

def main():
    maison = Maison("bleue", 780)
    thomas = Personne("sdpoigfhjoifgsfh", maison)

    print(thomas.presenter_caracteristiques())
if __name__ == "__main__":
    main()