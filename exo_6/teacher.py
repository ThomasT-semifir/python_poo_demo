from exo_6 import Person

class Teacher(Person):
    def __init__(self, age, subject):
        super().__init__(age)
        self.__subject = subject

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self,value):
        self.__subject = value

    def explain(self):
        return f"{self.say_hello()}, explaination begins about {self.subject}"
    
    def foo(self, bar):
        print("depuis l'enfant")