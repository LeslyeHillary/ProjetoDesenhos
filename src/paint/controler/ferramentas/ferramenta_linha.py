from controler.ferramentas.ferramenta_estado import FerramentaDesenhoFigura
from models.linha import Linha

class FerramentaLinha(FerramentaDesenhoFigura):
    # Inicializa as coordenadas iniciais e a última linha criada
    def __init__(self):
        self.x_inicial = 0
        self.y_inicial = 0
        self.ultima_linha = None

    # Salva o ponto onde o desenho da linha começa
    def clique(self, evento, controlador):
        self.x_inicial = evento.x
        self.y_inicial = evento.y

        # Cria uma prévia da linha
        controlador.figura_temporaria = Linha(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.atualizar_tela()

    # Atualiza a prévia da linha enquanto o mouse é arrastado
    def arrastar(self, evento, controlador):
        controlador.figura_temporaria = Linha(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.atualizar_tela()

    # Finaliza a linha e a adiciona ao desenho
    def soltar(self, evento, controlador):
        nova_linha = Linha(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )

        # Remove a linha anterior, se existir
        if self.ultima_linha is not None:
            controlador.desenho.remover_figura(self.ultima_linha)

        # Guarda a nova linha como a última criada
        self.ultima_linha = nova_linha

        controlador.desenho.adicionar_figura(nova_linha)

        # Remove a prévia da tela
        controlador.figura_temporaria = None

        # Atualiza a interface
        controlador.atualizar_tela()