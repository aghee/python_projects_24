from abc import ABC,abstractmethod
#make this class abstract to restrict creation of objects from it
class TransportMeans(ABC):
    def __init__(self,n):
        self.no_of_tyres=n
    @abstractmethod
    def ride(self):
        pass
    def showmessage(self):
        print('Showmessage called from the TransportMeans parent class!')
