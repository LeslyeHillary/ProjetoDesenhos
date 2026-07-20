from models.figuras import Figura

class Retangulo(Figura): # Representa um retangulo
    def desenhar(self, canvas, is_temporary=False):
        canvas.create_rectangle(
            self.x_inicial, self.y_inicial, self.x_final, self.y_final,
            outline=self.cor_borda, fill=self.cor_preenchimento
        )
