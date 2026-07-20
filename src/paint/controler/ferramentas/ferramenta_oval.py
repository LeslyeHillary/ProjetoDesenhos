from controler.ferramentas.ferramenta_estado import FerramentaDesenhoFigura
from models.oval import Oval

class FerramentaOval(FerramentaDesenhoFigura):
    # Inicializa as coordenadas do ponto inicial
    def __init__(self):
        self.x_inicial = 0
        self.y_inicial = 0

    # Guarda a posição onde o usuário iniciou o desenho
    def clique(self, evento, controlador):
        self.x_inicial = evento.x
        self.y_inicial = evento.y

        # Cria uma prévia do oval
        controlador.figura_temporaria = Oval(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.atualizar_tela()

    # Atualiza a prévia enquanto o mouse é movimentado
    def arrastar(self, evento, controlador):
        controlador.figura_temporaria = Oval(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.atualizar_tela()

    # Finaliza o oval e adiciona ao desenho
    def soltar(self, evento, controlador):
        figura = Oval(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.desenho.adicionar_figura(figura)

        # Remove a figura temporária
        controlador.figura_temporaria = None

        # Atualiza a interface
        controlador.atualizar_tela()