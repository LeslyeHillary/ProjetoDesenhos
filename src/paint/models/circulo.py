from models.figuras import Figura

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
