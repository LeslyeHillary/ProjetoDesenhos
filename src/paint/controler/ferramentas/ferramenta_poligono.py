from controler.ferramentas.ferramenta_estado import FerramentaDesenhoFigura
from models.poligono import Poligono

class FerramentaPoligono(FerramentaDesenhoFigura):
    def __init__(self):
        self.figura_poligono = None

    def clique(self, evento, controlador):
        cor_borda = controlador.obter_cor_borda()
        cor_preenchimento = controlador.obter_cor_preenchimento()

        if self.figura_poligono is None:
            self.figura_poligono = Poligono(cor_borda, cor_preenchimento)
            self.figura_poligono.adicionar_ponto(evento.x, evento.y)
            self.figura_poligono.adicionar_ponto(evento.x, evento.y)
        else:
            self.figura_poligono.pontos[-1] = (evento.x, evento.y)
            self.figura_poligono.adicionar_ponto(evento.x, evento.y)

        controlador.figura_temporaria = self.figura_poligono
        controlador.atualizar_tela()

    def movimentar(self, evento, controlador):
        if self.figura_poligono is not None:
            self.figura_poligono.pontos[-1] = (evento.x, evento.y)
            controlador.atualizar_tela()

    def duplo_clique(self, evento, controlador):
        if self.figura_poligono is None:
            return

        if len(self.figura_poligono.pontos) > 0:
            self.figura_poligono.pontos.pop()

        pontos_limpos = []
        for pt in self.figura_poligono.pontos:
            if not pontos_limpos or pontos_limpos[-1] != pt:
                pontos_limpos.append(pt)
        self.figura_poligono.pontos = pontos_limpos

        if len(self.figura_poligono.pontos) >= 3:
            controlador.desenho.adicionar_figura(self.figura_poligono)

        self.figura_poligono = None
        controlador.figura_temporaria = None
        controlador.atualizar_tela()
    def arrastar(self, evento, controlador):
        pass

    def soltar(self, evento, controlador):
        pass
