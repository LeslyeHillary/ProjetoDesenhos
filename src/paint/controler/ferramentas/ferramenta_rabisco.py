from controler.ferramentas.ferramenta_estado import FerramentaDesenhoFigura
from models.rabisco import Rabisco

class FerramentaRabisco(FerramentaDesenhoFigura):
    # Inicializa a variável que armazenará o rabisco em criação
    def __init__(self):
        self.figura_atual = None

    # Cria um novo rabisco no ponto onde o mouse foi pressionado
    def clique(self, evento, controlador):
        self.figura_atual = Rabisco(
            evento.x, evento.y, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.figura_temporaria = self.figura_atual
        controlador.atualizar_tela()

    # Adiciona novos pontos ao rabisco durante o movimento do mouse
    def arrastar(self, evento, controlador):
        if self.figura_atual:
            self.figura_atual.adicionar_ponto(evento.x, evento.y)
            controlador.atualizar_tela()

    # Finaliza o rabisco e o adiciona ao desenho
    def soltar(self, evento, controlador):
        if self.figura_atual:
            self.figura_atual.adicionar_ponto(evento.x, evento.y)
            controlador.desenho.adicionar_figura(self.figura_atual)

            # Limpa a figura temporária
            self.figura_atual = None
            controlador.figura_temporaria = None

            # Atualiza a interface
            controlador.atualizar_tela()