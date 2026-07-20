from abc import ABC, abstractmethod
# Importa a classe abstrata ABC, utilizada para criar uma classe base

class Figura(ABC):
    def __init__(self, x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento):
        # Coordenadas inicial e final da figura
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.x_final = x_final
        self.y_final = y_final
        # Cores da borda e do preenchimento
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    # Método que toda figura deve implementar para se desenhar na tela
    @abstractmethod
    def desenhar(self, canvas, is_temporary=False):
        pass
