from controler.ferramentas.ferramenta_estado import FerramentaDesenhoFigura
from models.poligono import Poligono

class FerramentaPoligono(FerramentaDesenhoFigura):
    # Inicializa a variável que armazenará o polígono em criação
    def __init__(self):
        self.figura_poligono = None

    # Adiciona um novo ponto ao polígono
    def clique(self, evento, controlador):
        cor_borda = controlador.obter_cor_borda()
        cor_preenchimento = controlador.obter_cor_preenchimento()

        # Cria um novo polígono no primeiro clique
        if self.figura_poligono is None:
            self.figura_poligono = Poligono(cor_borda, cor_preenchimento)
            self.figura_poligono.adicionar_ponto(evento.x, evento.y)
            self.figura_poligono.adicionar_ponto(evento.x, evento.y)
        else:
            # Atualiza o último ponto e adiciona um novo vértice
            self.figura_poligono.pontos[-1] = (evento.x, evento.y)
            self.figura_poligono.adicionar_ponto(evento.x, evento.y)

        controlador.figura_temporaria = self.figura_poligono
        controlador.atualizar_tela()

    # Move o último ponto para mostrar a prévia do polígono
    def movimentar(self, evento, controlador):
        if self.figura_poligono is not None:
            self.figura_poligono.pontos[-1] = (evento.x, evento.y)
            controlador.atualizar_tela()

    # Finaliza o polígono com um duplo clique
    def duplo_clique(self, evento, controlador):
        if self.figura_poligono is None:
            return

        # Remove o ponto temporário
        if len(self.figura_poligono.pontos) > 0:
            self.figura_poligono.pontos.pop()

        # Elimina pontos repetidos
        pontos_limpos = []
        for pt in self.figura_poligono.pontos:
            if not pontos_limpos or pontos_limpos[-1] != pt:
                pontos_limpos.append(pt)
        self.figura_poligono.pontos = pontos_limpos

        # Salva o polígono se ele possuir pelo menos três pontos
        if len(self.figura_poligono.pontos) >= 3:
            controlador.desenho.adicionar_figura(self.figura_poligono)

        # Limpa a figura temporária
        self.figura_poligono = None
        controlador.figura_temporaria = None
        controlador.atualizar_tela()

    # Não é utilizado para esta ferramenta
    def arrastar(self, evento, controlador):
        pass

    # Não é utilizado para esta ferramenta
    def soltar(self, evento, controlador):
        pass