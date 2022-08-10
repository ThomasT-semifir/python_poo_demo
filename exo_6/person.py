from abc import ABC, abstractmethod

class Person(ABC):
    '''
    les classes abstraites obligent celles qui en héritent à implémenter leurs méthodes abstraites
    une classe abstraite ne peut être instanciée
    '''
    def __init__(self, age: int):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value

    def say_hello(self):
        return "Hello!"

    @abstractmethod
    def foo(self, bar):
        '''
            une méthode  est comme une méthode static a l'exception que la classe doit être instanciée
        '''
        print("I'm abstract")
