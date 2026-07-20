import pickle

class ControladorDesenho:
    # Método responsável por inicializar os atributos da classe
    def __init__(self, desenho, obter_cor_borda, obter_cor_preenchimento, atualizar_tela):
        self.desenho = desenho
        self.obter_cor_borda = obter_cor_borda
        self.obter_cor_preenchimento = obter_cor_preenchimento
        self.atualizar_tela = atualizar_tela

        self.estado_ferramenta = None
        self.figura_temporaria = None

    def selecionar_ferramenta(self, ferramenta_instancia):
        self.estado_ferramenta = ferramenta_instancia

    def clique(self, evento):
        if self.estado_ferramenta:
            self.estado_ferramenta.clique(evento, self)

    def arrastar(self, evento):
        if self.estado_ferramenta:
            self.estado_ferramenta.arrastar(evento, self)

    def soltar(self, evento):
        if self.estado_ferramenta:
            self.estado_ferramenta.soltar(evento, self)

    def movimentar(self, evento):
        if self.estado_ferramenta:
            self.estado_ferramenta.movimentar(evento, self)

    def duplo_clique(self, evento):
        if self.estado_ferramenta:
            self.estado_ferramenta.duplo_clique(evento, self)

    def salvar_desenho(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, 'wb') as arquivo:
                # Armazena todas as figuras existentes no arquivo utilizando o pickle
                pickle.dump(self.desenho.figuras, arquivo)
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False

    def carregar_desenho(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, 'rb') as arquivo:
                figuras_salvas = pickle.load(arquivo)

            # Remove todas as figuras que já estavam no desenho atual
            self.desenho.figuras.clear()

            # Insere no desenho as figuras recuperadas do arquivo
            self.desenho.figuras = figuras_salvas

            # Atualiza a interface para exibir o desenho carregado
            self.atualizar_tela()
            return True
        except Exception as e:
            # Exibe no terminal a descrição do erro ocorrido durante o carregamento
            print(f"Erro ao carregar: {e}")
            return False