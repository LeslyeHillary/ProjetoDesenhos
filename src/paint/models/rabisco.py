from models.mao_livre import MaoLivre

class Rabisco(MaoLivre): # Representa um rabisco e herda comportamento de Maolivre
    def desenhar(self, canvas, is_temporary=False):
        if len(self.pontos) > 1:
            if is_temporary:
                canvas.create_line(self.coordenadas(), fill=self.cor_borda, dash=(4, 4))
            else:
                canvas.create_line(self.coordenadas(), fill=self.cor_borda, smooth=False)
