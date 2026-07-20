from models.mao_livre import MaoLivre

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
