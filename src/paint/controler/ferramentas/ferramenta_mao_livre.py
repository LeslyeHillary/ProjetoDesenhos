from controler.ferramentas.ferramenta_estado import FerramentaDesenhoFigura
from models.mao_livre import MaoLivre

class FerramentaMaoLivre(FerramentaDesenhoFigura):
    def __init__(self):
        self.figura_atual = None

    def clique(self, evento, controlador):
        self.figura_atual = MaoLivre(
            evento.x, evento.y, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.figura_temporaria = self.figura_atual
        controlador.atualizar_tela()

    def arrastar(self, evento, controlador):
        if self.figura_atual:
            self.figura_atual.adicionar_ponto(evento.x, evento.y)
            controlador.atualizar_tela()

    def soltar(self, evento, controlador):
        if self.figura_atual:
            self.figura_atual.adicionar_ponto(evento.x, evento.y)
            controlador.desenho.adicionar_figura(self.figura_atual)
            
            self.figura_atual = None
            controlador.figura_temporaria = None
            controlador.atualizar_tela()
