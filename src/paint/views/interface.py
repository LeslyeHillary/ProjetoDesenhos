import tkinter as tk
from tkinter.colorchooser import askcolor
from controler.controlador import ControladorDesenho
from models.desenho import Desenho

# Classe responsável pela interface gráfica do MVC
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

    def _configurar_janela(self): # Define tamanho da janela e centraliza 
        largura, altura = 900, 600
        tela_largura = self.janela.winfo_screenwidth()
        tela_altura = self.janela.winfo_screenheight()

        # Resolução da tela
        x = (tela_largura - largura) // 2
        y = (tela_altura - altura) // 2

        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")

    def criar_widgets(self): # Cria todos os componentes da interface
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

        # Dicionário/Lista mapeando o Nome do Botão para a string da ferramenta
        ferramentas = [
            ("Retângulo", "retangulo"),
            ("Oval", "oval"),
            ("Círculo", "circulo"),
            ("Polígono", "poligono"),
            ("Mão livre", "mao_livre"),
            ("Linha", "linha"),
            ("Rabisco", "rabisco"),
        ]

        # Cria os botões de ferramentas automaticamente com 'lambda'
        for texto, nome_ferramenta in ferramentas:
            tk.Button(
                barra,
                text=texto,
                # O `lambda f=nome_ferramenta:` captura o valor da string e passa direto
                command=lambda f=nome_ferramenta: self._trocar_ferramenta(f),
                **estilo_botao
            ).pack(side="left")
            
        # Os botões de cor mantêm seus comandos separados pois executam lógicas diferentes
        tk.Button(barra, text="Cor da borda", command=self.mudar_borda, **estilo_botao).pack(side="left")
        tk.Button(barra, text="Cor preenchimento", command=self.mudar_preenchimento, **estilo_botao).pack(side="left")


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
        # Eventos especificos
        self.canvas.bind("<Double-Button-1>", self.controlador.duplo_clique)
        self.canvas.bind("<Motion>", self.controlador.movimentar)

    def atualizar_tela(self): # Apaga e redesenha todas as figuras presentes no modelo
        self.canvas.delete("all")
        
        for figura in self.desenho.figuras:
            figura.desenhar(self.canvas, is_temporary=False)
            
        if self.controlador.figura_temporaria:
            self.controlador.figura_temporaria.desenhar(self.canvas, is_temporary=True)

    def _trocar_ferramenta(self, ferramenta): # Atualiza a ferramenta atualmente selecionada
        self.ferramenta = ferramenta
        if self.controlador:
            self.controlador.selecionar_ferramenta(ferramenta)

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