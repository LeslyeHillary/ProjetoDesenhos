class ControladorDesenho:
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