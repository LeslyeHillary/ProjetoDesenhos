import tkinter as tk

from eventos import clique, arrastar, soltar
from cores import escolher_cor_borda, escolher_cor_preenchimento

# Variáveis principais da interface
janela = None
canvas = None

# Ferramenta escolhida no momento
ferramenta = "retangulo"

# Cores padrão usadas no desenho
cor_borda = "black"
cor_preenchimento = "white"


# Escolhe a ferramenta de retângulo
def selecionar_retangulo():
    global ferramenta
    ferramenta = "retangulo"

# Escolhe a ferramenta de oval
def selecionar_oval():
    global ferramenta
    ferramenta = "oval"

# Escolhe a ferramenta de círculo
def selecionar_circulo():
    global ferramenta
    ferramenta = "circulo"

# Muda a cor da borda
def mudar_borda():
    global cor_borda
    cor_borda = escolher_cor_borda()

# Muda a cor de preenchimento
def mudar_preenchimento():
    global cor_preenchimento
    cor_preenchimento = escolher_cor_preenchimento()


# Cria e mostra a janela principal do programa
def iniciar():
    global janela
    global canvas

    janela = tk.Tk()
    janela.title("Paint Imperativo")
    janela.geometry("900x600")

    # Barra com os botões de ferramentas e cores
    barra = tk.Frame(janela)
    barra.pack(fill="x")

    tk.Button(barra, text="Retângulo", command=selecionar_retangulo).pack(side="left")
    tk.Button(barra, text="Oval", command=selecionar_oval).pack(side="left")
    tk.Button(barra, text="Círculo", command=selecionar_circulo).pack(side="left")
    tk.Button(barra, text="Cor da borda", command=mudar_borda).pack(side="left")
    tk.Button(barra, text="Cor preenchimento", command=mudar_preenchimento).pack(side="left")

    # Área onde as formas serão desenhadas
    canvas = tk.Canvas(janela, bg="white")
    canvas.pack(fill="both", expand=True)

    # Conecta as ações feitas com o mouse às funções de desenho
    canvas.bind("<Button-1>", clique)
    canvas.bind("<B1-Motion>", arrastar)
    canvas.bind("<ButtonRelease-1>", soltar)

    janela.mainloop()