# Importa todas as classes de figuras utilizadas pelo controlador
from models.figuras import (
    Circulo,
    Linha,
    MaoLivre,
    Oval,
    Poligono,
    Rabisco,
    Retangulo,
)

class ControladorDesenho: #Classe responsável por controlar toda a lógica de desenho da aplicação, recebe os eventos do mouse, cria as figuras e atualiza o modelo e a interface.
    def __init__(self, desenho, obter_cor_borda, obter_cor_preenchimento, atualizar_tela):
        self.desenho = desenho  # Modelo onde as figuras serão armazenadas
        
		 # Funções que retornam as cores atualmente selecionadas
        self.obter_cor_borda = obter_cor_borda
        self.obter_cor_preenchimento = obter_cor_preenchimento
        

        self.atualizar_tela = atualizar_tela   # Função utilizada para redesenhar a tela
        self.ferramenta = "retangulo"  #Ferramenta selecionada inicialmente

        self.x_inicial = 0
        self.y_inicial = 0

        self.figura_temporaria = None 
        self.figura_mao_livre = None
        self.figura_poligono = None  
        self.ultima_linha = None

    def selecionar_ferramenta(self, ferramenta): # Altera a ferramenta atualmente selecionada, caso um polígono esteja sendo criado, ele é finalizado.
        if self.ferramenta == "poligono" and ferramenta != "poligono" and self.figura_poligono is not None:
            self.finalizar_poligono()
        self.ferramenta = ferramenta

    def clique(self, evento): #Executado quando o botão esquerdo do mouse é pressionado.


        if self.ferramenta != "poligono" and self.figura_poligono is not None: # Finaliza um polígono caso outra ferramenta seja utilizada
            self.finalizar_poligono()

        self.x_inicial = evento.x
        self.y_inicial = evento.y

        if self.ferramenta == "poligono": # Tratamento específico para polígonos
            self._lidar_clique_poligono(evento)
            return
            
        if self.ferramenta not in ("mao_livre", "rabisco"): # Tratamento específico para mao livre e rabisco
            self.figura_temporaria = self._criar_figura(evento.x, evento.y)
            self.atualizar_tela()
            return

        cor_borda = self.obter_cor_borda()
        cor_preenchimento = self.obter_cor_preenchimento()

        figura = MaoLivre if self.ferramenta == "mao_livre" else Rabisco

        self.figura_mao_livre = figura(
            evento.x, evento.y, evento.x, evento.y, cor_borda, cor_preenchimento
        )
        self.figura_temporaria = self.figura_mao_livre
        self.atualizar_tela()

    def _lidar_clique_poligono(self, evento): #Adiciona um novo vértice ao polígono.

        cor_borda = self.obter_cor_borda()
        cor_preenchimento = self.obter_cor_preenchimento()

        if self.figura_poligono is None:
            self.figura_poligono = Poligono(cor_borda, cor_preenchimento)
            self.figura_poligono.adicionar_ponto(evento.x, evento.y)
            self.figura_poligono.adicionar_ponto(evento.x, evento.y)
        else:
            self.figura_poligono.pontos[-1] = (evento.x, evento.y)
            self.figura_poligono.adicionar_ponto(evento.x, evento.y)

        self.figura_temporaria = self.figura_poligono
        self.atualizar_tela()

    def movimentar(self, evento): #Atualiza a pré-visualização do último lado do polígono enquanto o mouse é movimentado.
        if self.ferramenta == "poligono" and self.figura_poligono is not None:
            self.figura_poligono.pontos[-1] = (evento.x, evento.y)
            self.atualizar_tela()

    def arrastar(self, evento): # Executado enquanto o mouse é arrastado.
        if self.ferramenta == "poligono":
            return 

        if self.ferramenta in ("mao_livre", "rabisco"):
            if self.figura_mao_livre is None:
                self.clique(evento)

            self.figura_mao_livre.adicionar_ponto(evento.x, evento.y)
            self.atualizar_tela()
            return

        self.figura_temporaria = self._criar_figura(evento.x, evento.y)
        self.atualizar_tela()

    def soltar(self, evento): #Executado quando o botão do mouse é liberado.
        if self.ferramenta == "poligono":
            return  

        if self.ferramenta in ("mao_livre", "rabisco"):
            if self.figura_mao_livre is None:
                return

            self.figura_mao_livre.adicionar_ponto(evento.x, evento.y)
            self.desenho.adicionar_figura(self.figura_mao_livre)
            self.figura_mao_livre = None
            self.figura_temporaria = None
            self.atualizar_tela()
            return

        figura = self._criar_figura(evento.x, evento.y)

        if self.ferramenta == "linha":
            if self.ultima_linha is not None:
                self.desenho.remover_figura(self.ultima_linha)
            self.ultima_linha = figura

        self.desenho.adicionar_figura(figura)
        self.figura_temporaria = None
        self.atualizar_tela()

    def duplo_clique(self, evento):  #Finaliza o polígono quando ocorre um duplo clique
        if self.ferramenta == "poligono" and self.figura_poligono is not None:
            self.finalizar_poligono()

    def finalizar_poligono(self): #Finaliza a construção do polígono e o adiciona ao desenho.
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
            self.desenho.adicionar_figura(self.figura_poligono)

        self.figura_poligono = None
        self.figura_temporaria = None
        self.atualizar_tela()

    def _criar_figura(self, x_final, y_final): # Cria uma figura de acordo com a ferramenta selecionada.
        cor_borda = self.obter_cor_borda()
        cor_preenchimento = self.obter_cor_preenchimento()

        figuras = {
            "retangulo": Retangulo,
            "oval": Oval,
            "circulo": Circulo,
            "linha": Linha,
        }

        if self.ferramenta == "poligono":
            return Poligono(cor_borda, cor_preenchimento)

		# Relaciona o nome da ferramenta à sua classe
        figura = figuras.get(self.ferramenta, Retangulo)

        return figura(
            self.x_inicial,
            self.y_inicial,
            x_final,
            y_final,
            cor_borda,
            cor_preenchimento,
        )
