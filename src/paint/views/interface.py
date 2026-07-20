import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import filedialog, messagebox  # <-- 1. IMPORTAÇÕES ADICIONADAS AQUI

from controler.controlador import ControladorDesenho
from models.desenho import Desenho

# Importando todas as classes de ferramentas
from controler.ferramentas.ferramenta_retangulo import FerramentaRetangulo
from controler.ferramentas.ferramenta_oval import FerramentaOval
from controler.ferramentas.ferramenta_circulo import FerramentaCirculo
from controler.ferramentas.ferramenta_poligono import FerramentaPoligono
from controler.ferramentas.ferramenta_mao_livre import FerramentaMaoLivre
from controler.ferramentas.ferramenta_linha import FerramentaLinha
from controler.ferramentas.ferramenta_rabisco import FerramentaRabisco

# Classe responsável pela interface gráfica do MVC
class InterfaceGrafica:
    def __init__(self):  # <-- CORRIGIDO PARA DOIS UNDERLINES (__init__)
        # Cria a janela principal
        self.janela = tk.Tk()
        self.janela.title("Paint MVC")

        self._configurar_janela()

        self.desenho = Desenho()
        self.canvas = None
        self.controlador = None

        # Ferramenta inicial agora é uma instância da classe, não uma string
        self.ferramenta = FerramentaRetangulo()
        self.cor_borda = "black"
        self.cor_preenchimento = "white"

    def _configurar_janela(self): 
        largura, altura = 900, 600
        tela_largura = self.janela.winfo_screenwidth()
        tela_altura = self.janela.winfo_screenheight()

        x = (tela_largura - largura) // 2
        y = (tela_altura - altura) // 2

        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")

    def criar_widgets(self): 
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

        # Lista com as instâncias das ferramentas
        ferramentas = [
            ("Retângulo", FerramentaRetangulo()),
            ("Oval", FerramentaOval()),
            ("Círculo", FerramentaCirculo()),
            ("Polígono", FerramentaPoligono()),
            ("Mão livre", FerramentaMaoLivre()),
            ("Linha", FerramentaLinha()),
            ("Rabisco", FerramentaRabisco()),
        ]

        # Cria os botões passando a instância da ferramenta (o objeto)
        for texto, ferramenta_instancia in ferramentas:
            tk.Button(
                barra,
                text=texto,
                command=lambda f=ferramenta_instancia: self._trocar_ferramenta(f),
                **estilo_botao
            ).pack(side="left")
            
        tk.Button(barra, text="Cor da borda", command=self.mudar_borda, **estilo_botao).pack(side="left")
        tk.Button(barra, text="Cor preenchimento", command=self.mudar_preenchimento, **estilo_botao).pack(side="left")

        # <-- 2. BOTÕES DE SALVAR E ABRIR ADICIONADOS AQUI -->
        tk.Button(barra, text="💾 Salvar", command=self.salvar_arquivo, **estilo_botao).pack(side="right", padx=2)
        tk.Button(barra, text="📂 Abrir", command=self.abrir_arquivo, **estilo_botao).pack(side="right", padx=2)

        self.canvas = tk.Canvas(self.janela, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # Cria o controlador
        self.controlador = ControladorDesenho(
            self.desenho,
            lambda: self.cor_borda,
            lambda: self.cor_preenchimento,
            self.atualizar_tela
        )

        # Seleciona a ferramenta inicial
        self.controlador.selecionar_ferramenta(self.ferramenta)

        # Binds do mouse
        self.canvas.bind("<Button-1>", self.controlador.clique)
        self.canvas.bind("<B1-Motion>", self.controlador.arrastar)
        self.canvas.bind("<ButtonRelease-1>", self.controlador.soltar)
        self.canvas.bind("<Double-Button-1>", self.controlador.duplo_clique)
        self.canvas.bind("<Motion>", self.controlador.movimentar)

    def atualizar_tela(self): 
        self.canvas.delete("all")
        
        for figura in self.desenho.figuras:
            figura.desenhar(self.canvas, is_temporary=False)
            
        if self.controlador.figura_temporaria:
            self.controlador.figura_temporaria.desenhar(self.canvas, is_temporary=True)

    def _trocar_ferramenta(self, ferramenta): 
        self.ferramenta = ferramenta
        if self.controlador:
            self.controlador.selecionar_ferramenta(ferramenta)

    def mudar_borda(self):
        cor = askcolor(title="Escolha a cor da borda")[1]
        if cor:
            self.cor_borda = cor

    def mudar_preenchimento(self):
        cor = askcolor(title="Escolha a cor de preenchimento")[1]
        if cor:
            self.cor_preenchimento = cor

    # <-- 3. FUNÇÕES DE ARQUIVO ADICIONADAS AQUI -->
    def salvar_arquivo(self):
        # Abre a janela pedindo onde o usuário quer salvar
        caminho = filedialog.asksaveasfilename(
            defaultextension=".pnt",
            filetypes=[("Arquivos Paint MVC", "*.pnt"), ("Todos os Arquivos", "*.*")],
            title="Salvar Desenho"
        )
        if caminho: # Se o usuário não cancelou a janela
            sucesso = self.controlador.salvar_desenho(caminho)
            if sucesso:
                messagebox.showinfo("Sucesso", "Desenho salvo com sucesso!")
            else:
                messagebox.showerror("Erro", "Não foi possível salvar o desenho.")

    def abrir_arquivo(self):
        # Abre a janela pedindo qual arquivo abrir
        caminho = filedialog.askopenfilename(
            filetypes=[("Arquivos Paint MVC", "*.pnt"), ("Todos os Arquivos", "*.*")],
            title="Abrir Desenho"
        )
        if caminho: # Se o usuário selecionou algo
            sucesso = self.controlador.carregar_desenho(caminho)
            if sucesso:
                messagebox.showinfo("Sucesso", "Desenho carregado com sucesso!")
            else:
                messagebox.showerror("Erro", "Não foi possível carregar o arquivo ou o formato é inválido.")

    def executar(self):
        self.criar_widgets()
        self.janela.mainloop()

def iniciar():
    interface = InterfaceGrafica()
    interface.executar()