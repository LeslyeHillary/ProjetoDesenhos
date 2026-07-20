from models.figuras import Figura

class MaoLivre(Figura): # Representa um desenho feito a mao livre
    def __init__(self, x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento, iniciar_lista=True):
        super().__init__(x_inicial, y_inicial, x_final, y_final, cor_borda, cor_preenchimento)

        if iniciar_lista:
            self.pontos = [
                (x_inicial, y_inicial),
                (x_final, y_final),
            ]
        else:
            self.pontos = []

    def adicionar_ponto(self, x, y): # Adiciona novo ponto ao desenho
        self.x_final = x
        self.y_final = y
        self.pontos.append((x, y))

    def coordenadas(self): # Converte a lista de pontos para o formato utilizado pelo Tkinter
        coordenadas = []
        for ponto in self.pontos:
            coordenadas.extend(ponto)
        return coordenadas

    def desenhar(self, canvas, is_temporary=False):
        if len(self.pontos) > 1:
            canvas.create_line(self.coordenadas(), fill=self.cor_borda, smooth=True)
