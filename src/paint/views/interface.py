import tkinter as tk
from tkinter.colorchooser import askcolor
from controler.controlador import ControladorDesenho
from models.desenho import Desenho



#classe responsavel pela interface gráfica do MVC
class InterfaceGrafica:
    def __init__(self):
        # Cria a janela principal
        self.janela = tk.Tk()
        self.janela.title("Paint MVC")


        self._configurar_janela()


        self.desenho = Desenho()
        self.canvas = None
        self.controlador = None


        self.ferramenta = "retangulo"
        self.cor_borda = "black"
        self.cor_preenchimento = "white"


    def _configurar_janela(self): #define tamanho da janela e centraliza 
        largura, altura = 900, 600


        tela_largura = self.janela.winfo_screenwidth()
        tela_altura = self.janela.winfo_screenheight()

        #resolução da tela
        x = (tela_largura - largura) // 2
        y = (tela_altura - altura) // 2


        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")


    def criar_widgets(self):#cria todos os componentes da interface
        
        # Barra superior para os botões
        barra = tk.Frame(self.janela)
        barra.pack(fill="x")


        estilo_botao = {
            "bg": "#D8B4FE",
            "fg": "black",
            "activebackground": "#C084FC",
            "activeforeground": "black",
            "highlightthickness": 1,
            "highlightbackground": "#B794F4",
            "bd": 1,
            "relief": "raised",
        }

        # Lista contendo texto do botão e função correspondente
        botoes = [
            ("Retângulo", self.selecionar_retangulo),
            ("Oval", self.selecionar_oval),
            ("Círculo", self.selecionar_circulo),
            ("Polígono", self.selecionar_poligono),
            ("Mão livre", self.selecionar_mao_livre),
            ("Linha", self.selecionar_linha),
            ("Rabisco", self.selecionar_rabisco),
            ("Cor da borda", self.mudar_borda),
            ("Cor preenchimento", self.mudar_preenchimento),
        ]

        # Cria todos os botões automaticamente
        for texto, comando in botoes:
            tk.Button(
                barra,
                text=texto,
                command=comando,
                **estilo_botao
            ).pack(side="left")


        self.canvas = tk.Canvas(self.janela, bg="white")
        self.canvas.pack(fill="both", expand=True)

         # Cria o controlador
        self.controlador = ControladorDesenho(
            self.desenho,
            lambda: self.cor_borda,
            lambda: self.cor_preenchimento,
            self.atualizar_tela
        )


        self.controlador.selecionar_ferramenta(self.ferramenta)

        # Liga os eventos do mouse aos métodos do controlador
        self.canvas.bind("<Button-1>", self.controlador.clique)
        self.canvas.bind("<B1-Motion>", self.controlador.arrastar)
        self.canvas.bind("<ButtonRelease-1>", self.controlador.soltar)
        #eventos especificos
        self.canvas.bind("<Double-Button-1>", self.controlador.duplo_clique)
        self.canvas.bind("<Motion>", self.controlador.movimentar)


    def atualizar_tela(self): #Apaga e redesenha todas as figuras presentes no modelo
        self.canvas.delete("all")
       
        for figura in self.desenho.figuras:
            self._desenhar_figura(figura, is_temporary=False)
           
        if self.controlador.figura_temporaria:
            self._desenhar_figura(self.controlador.figura_temporaria, is_temporary=True)


    def _desenhar_figura(self, figura, is_temporary):#Desenha uma figura de acordo com seu tipo.
        from models.figuras import Retangulo, Oval, Circulo, Poligono, MaoLivre, Linha, Rabisco


        if isinstance(figura, Retangulo):
            self.canvas.create_rectangle(
                figura.x_inicial, figura.y_inicial, figura.x_final, figura.y_final,
                outline=figura.cor_borda, fill=figura.cor_preenchimento
            )
        elif isinstance(figura, Oval):
            self.canvas.create_oval(
                figura.x_inicial, figura.y_inicial, figura.x_final, figura.y_final,
                outline=figura.cor_borda, fill=figura.cor_preenchimento
            )
        elif isinstance(figura, Circulo):
            x1, y1, x2, y2 = figura.coordenadas_ajustadas()
            self.canvas.create_oval(
                x1, y1, x2, y2,
                outline=figura.cor_borda, fill=figura.cor_preenchimento
            )
        elif isinstance(figura, Poligono):
            coords = figura.coordenadas()
            if len(figura.pontos) >= 3:
                self.canvas.create_polygon(coords, outline=figura.cor_borda, fill=figura.cor_preenchimento)
            elif len(figura.pontos) == 2:
                self.canvas.create_line(coords, fill=figura.cor_borda)
        elif isinstance(figura, Linha):
            self.canvas.create_line(
                figura.x_inicial, figura.y_inicial, figura.x_final, figura.y_final,
                fill=figura.cor_borda
            )
        elif isinstance(figura, (MaoLivre, Rabisco)):
            if len(figura.pontos) > 1:
                if isinstance(figura, Rabisco) and is_temporary:
                    self.canvas.create_line(figura.coordenadas(), fill=figura.cor_borda, dash=(4, 4))
                else:
                    suave = isinstance(figura, MaoLivre)
                    self.canvas.create_line(figura.coordenadas(), fill=figura.cor_borda, smooth=suave)


    def _trocar_ferramenta(self, ferramenta): #Atualiza a ferramenta atualmente selecionada
        self.ferramenta = ferramenta


        if self.controlador: # Informa ao controlador qual ferramenta será utilizada
            self.controlador.selecionar_ferramenta(ferramenta)

     # Métodos chamados pelos botões
    def selecionar_retangulo(self):
        self._trocar_ferramenta("retangulo")


    def selecionar_oval(self):
        self._trocar_ferramenta("oval")


    def selecionar_circulo(self):
        self._trocar_ferramenta("circulo")


    def selecionar_poligono(self):
        self._trocar_ferramenta("poligono")


    def selecionar_mao_livre(self):
        self._trocar_ferramenta("mao_livre")


    def selecionar_linha(self):
        self._trocar_ferramenta("linha")


    def selecionar_rabisco(self):
        self._trocar_ferramenta("rabisco")


    def mudar_borda(self): # Permite escolher a cor da borda.

        cor = askcolor(title="Escolha a cor da borda")[1]
        if cor is not None:
            self.cor_borda = cor
        else:
            self.cor_borda = "black"


    def mudar_preenchimento(self): # Permite escolher a cor do preenchimento
        cor = askcolor(title="Escolha a cor de preenchimento")[1]
        if cor is not None:
            self.cor_preenchimento = cor
        else:
            self.cor_preenchimento = "white"


    def executar(self):
        self.criar_widgets()
        self.janela.mainloop()


def iniciar():
    interface = InterfaceGrafica()
    interface.executar()