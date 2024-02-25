"""
Python by default does NOT support abstraction hence the need for abc module - abstract classes,abstract methods
Abstract classes-ABC - a class having one or more abstract methods
An abstract class is derived from ABC class that belongs to abc module 
An abstract class can have normal methods(methods without @abstractmethod)
ABC,cannot instatiate abstract class,must have at least one abstract method
abstract methods-only declaration,no definition/implementation; @abstractmethod
abstract method in the abstract base class only show the functionality of the method but DO NOT implement the 
methods.The implementation of these methods must be done in the subclasses/childclass
Every class that extends from/inherits from abstract class must have its own implementation
of the abstract method declared in the abstract base class. If not then the childclass/derived class becomes an abstract class,
which means it has abstractclass properties eg you can't create an object of that class
If you are inheriting from a class,you must follow the rules of the parent/base class
"""

from abstract_class import TransportMeans

class Bike(TransportMeans):
    def __init__(self,n,color):
        super().__init__(n)
        self.color=color
    def ride(self):
        print(f'Started by a push to pedal!Bike has color {self.color} and {self.no_of_tyres} tyres')
class Scooter(TransportMeans):
    def __init__(self,n):
        super().__init__(n)
    def ride(self):
        print('Starts on its own!')
    def showmessage(self):
        print('Showmessage called from the Scooter child class! Method overriding')
class MotorCar(TransportMeans):
    def __init__(self,n,gears):
        super().__init__(n)
        self.gears=gears
    def ride(self):
        print(f'Starts using a key or pressing a button. It also has {self.gears} gears and {self.no_of_tyres} tyres')

    

