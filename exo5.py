from __future__ import annotations
from difflib import Match
import math

class Point:
    def __init__(self, abs, ord):
        self.__abs = abs
        self.__ord = ord

    @property
    def abs(self):
        return self.__abs
    
    @abs.setter
    def abs(self, value):
        self.__abs = value

    @property
    def ord(self):
        return self.__ord

    @ord.setter
    def ord(self, value):
        self.__ord = value
    
    def calculer_distance(self, autre_point: Point):
        return math.sqrt((self.abs - autre_point.abs)**2 + (self.ord - autre_point.ord) **2)