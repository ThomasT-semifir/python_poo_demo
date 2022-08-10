from __future__ import annotations

class Complex:

    def __init__(self, reel, imaginaire):
        self.__reel = reel
        self.__imaginaire = imaginaire

    # .. properties ...

    def addition_complex(self, autre_nombre: Complex):
        """Une documentation exhaustive et intéressante"""
        return Complex(self.__reel + autre_nombre.__reel, self.__imaginaire + autre_nombre.__imaginaire)

    def __add__(self, autre_complex: Complex):
        return self.addition_complex(autre_complex)

    def __str__(self):
        return f"{self.__reel}+{self.__imaginaire}i: {super().__str__()}"
complex = Complex(2,5)
print(complex)