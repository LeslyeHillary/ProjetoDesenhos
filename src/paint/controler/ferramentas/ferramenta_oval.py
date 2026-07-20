from controler.ferramentas.ferramenta_estado import FerramentaDesenhoFigura
from models.oval import Oval

class FerramentaOval(FerramentaDesenhoFigura):
    def __init__(self):
        self.x_inicial = 0
        self.y_inicial = 0

    def clique(self, evento, controlador):
        self.x_inicial = evento.x
        self.y_inicial = evento.y

        controlador.figura_temporaria = Oval(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.atualizar_tela()

    def arrastar(self, evento, controlador):
        controlador.figura_temporaria = Oval(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.atualizar_tela()

    def soltar(self, evento, controlador):
        figura = Oval(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.desenho.adicionar_figura(figura)
        controlador.figura_temporaria = None
        controlador.atualizar_tela()
