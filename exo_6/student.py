from exo_6 import Person


class Student(Person):
    def __init__(self, age):
        super().__init__(age)

    def display_age(self):
        return f"My age is: {self.age}"

    def go_to_class(self):
        return "I'm going to class"

    def hello_school(self):
        return f"{self.say_hello()}, {self.go_to_class()}"

    def foo(self, bar):
        print("depuis l'enfant : " )
        super().foo(bar)