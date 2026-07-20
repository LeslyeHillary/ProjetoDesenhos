from models.figuras import Figura

class Linha(Figura): # Representa uma linha
    def desenhar(self, canvas, is_temporary=False):
        canvas.create_line(
            self.x_inicial, self.y_inicial, self.x_final, self.y_final,
            fill=self.cor_borda
        )
