from abc import ABC, abstractmethod

class FerramentaDesenhoFigura(ABC):
    @abstractmethod
    def clique(self, evento, controlador):
        pass

    @abstractmethod
    def arrastar(self, evento, controlador):
        pass

    @abstractmethod
    def soltar(self, evento, controlador):
        pass
        
    def movimentar(self, evento, controlador):
        pass

    def duplo_clique(self, evento, controlador):
        pass
