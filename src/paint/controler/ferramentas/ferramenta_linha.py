from controler.ferramentas.ferramenta_estado import FerramentaDesenhoFigura
from models.linha import Linha

class FerramentaLinha(FerramentaDesenhoFigura):
    def __init__(self):
        self.x_inicial = 0
        self.y_inicial = 0
        self.ultima_linha = None 

    def clique(self, evento, controlador):
        self.x_inicial = evento.x
        self.y_inicial = evento.y
        controlador.figura_temporaria = Linha(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.atualizar_tela()

    def arrastar(self, evento, controlador):
        controlador.figura_temporaria = Linha(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.atualizar_tela()

    def soltar(self, evento, controlador):
        nova_linha = Linha(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )

        if self.ultima_linha is not None:
            controlador.desenho.remover_figura(self.ultima_linha)
            
        self.ultima_linha = nova_linha
        
        controlador.desenho.adicionar_figura(nova_linha)
        controlador.figura_temporaria = None
        controlador.atualizar_tela()
