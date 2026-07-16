from abc import ABC

class Figura(ABC):
    def __init__(self, x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento):
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.x_final = x_final
        self.y_final = y_final
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

class Retangulo(Figura):
    pass

class Oval(Figura):
    pass

class Circulo(Figura):
      def coordenadas_ajustadas(self):
            lado = min(abs(self.x_final - self.x_inicial), abs(self.y_final - self.y_inicial))

            if self.x_final < self.x_inicial:
                  x_final = self.x_inicial - lado
            else:
                  x_final = self.x_inicial + lado

            if self.y_final < self.y_inicial:
                  y_final = self.y_inicial - lado
            else:
                  y_final = self.y_inicial + lado

            return self.x_inicial, self.y_inicial, x_final, y_final

class MaoLivre(Figura):
    def __init__(
        self, x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento, iniciar_lista=True):
        super().__init__(
            x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

        if iniciar_lista:
            self.pontos = [
                (x_inicial, y_inicial),
                (x_final, y_final),
            ]
        else:
            self.pontos = []

    def adicionar_ponto(self, x, y):
        self.x_final = x
        self.y_final = y

        self.pontos.append((x, y))

    def coordenadas(self):
        coordenadas = []

        for ponto in self.pontos:
            coordenadas.extend(ponto)
        return coordenadas

class Poligono(MaoLivre):
    def __init__(self, cor_borda, cor_preenchimento):
        super().__init__(0, 0, 0, 0, cor_borda, cor_preenchimento, iniciar_lista=False)

    def adicionar_ponto(self, x, y):
        self.pontos.append((x, y))

class Linha(Figura):
    pass

class Rabisco(MaoLivre):
    pass
