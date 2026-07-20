from controler.ferramentas.ferramenta_estado import FerramentaDesenhoFigura
from models.retangulo import Retangulo

class FerramentaRetangulo(FerramentaDesenhoFigura):
    # Inicializa as coordenadas iniciais do retângulo
    def __init__(self):
        self.x_inicial = 0
        self.y_inicial = 0

    # Guarda o ponto onde o usuário iniciou o desenho
    def clique(self, evento, controlador):
        self.x_inicial = evento.x
        self.y_inicial = evento.y

        # Cria uma prévia do retângulo
        controlador.figura_temporaria = Retangulo(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.atualizar_tela()

    # Atualiza a prévia enquanto o mouse é arrastado
    def arrastar(self, evento, controlador):
        controlador.figura_temporaria = Retangulo(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.atualizar_tela()

    # Cria o retângulo definitivo e adiciona ao desenho
    def soltar(self, evento, controlador):
        figura = Retangulo(
            self.x_inicial, self.y_inicial, evento.x, evento.y,
            controlador.obter_cor_borda(), controlador.obter_cor_preenchimento()
        )
        controlador.desenho.adicionar_figura(figura)

        # Remove a prévia da tela
        controlador.figura_temporaria = None

        # Atualiza a interface
        controlador.atualizar_tela()