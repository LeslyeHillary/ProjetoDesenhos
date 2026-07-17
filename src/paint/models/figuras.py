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

    @abstractmethod
    def desenhar(self, canvas, is_temporary=False):
        """Método que toda figura deve implementar para se desenhar na tela"""
        pass

class Retangulo(Figura): # Representa um retangulo
    def desenhar(self, canvas, is_temporary=False):
        canvas.create_rectangle(
            self.x_inicial, self.y_inicial, self.x_final, self.y_final,
            outline=self.cor_borda, fill=self.cor_preenchimento
        )

class Oval(Figura): # Representa um oval
    def desenhar(self, canvas, is_temporary=False):
        canvas.create_oval(
            self.x_inicial, self.y_inicial, self.x_final, self.y_final,
            outline=self.cor_borda, fill=self.cor_preenchimento
        )

class Circulo(Figura): # Representa um circulo e garante que a largura e altura sejam iguais
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

    def desenhar(self, canvas, is_temporary=False):
        x1, y1, x2, y2 = self.coordenadas_ajustadas()
        canvas.create_oval(
            x1, y1, x2, y2,
            outline=self.cor_borda, fill=self.cor_preenchimento
        )

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

class Poligono(MaoLivre): # Representa um polígono formado por vários pontos
    def __init__(self, cor_borda, cor_preenchimento):
        super().__init__(0, 0, 0, 0, cor_borda, cor_preenchimento, iniciar_lista=False)

    def adicionar_ponto(self, x, y):
        self.pontos.append((x, y))

    def desenhar(self, canvas, is_temporary=False):
        coords = self.coordenadas()
        if len(self.pontos) >= 3:
            canvas.create_polygon(coords, outline=self.cor_borda, fill=self.cor_preenchimento)
        elif len(self.pontos) == 2:
            canvas.create_line(coords, fill=self.cor_borda)

class Linha(Figura): # Representa uma linha
    def desenhar(self, canvas, is_temporary=False):
        canvas.create_line(
            self.x_inicial, self.y_inicial, self.x_final, self.y_final,
            fill=self.cor_borda
        )

class Rabisco(MaoLivre): # Representa um rabisco e herda comportamento de Maolivre
    def desenhar(self, canvas, is_temporary=False):
        if len(self.pontos) > 1:
            if is_temporary:
                canvas.create_line(self.coordenadas(), fill=self.cor_borda, dash=(4, 4))
            else:
                canvas.create_line(self.coordenadas(), fill=self.cor_borda, smooth=False)