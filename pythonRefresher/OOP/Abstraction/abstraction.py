# the meaning of abstraction is to hide the complexity and only show the essential features of the object.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("The engine is starting...")

    def stop_engine(self):
        print("The engine is stopping...")