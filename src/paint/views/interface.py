import tkinter as tk

from eventos import ControladorDesenho
from cores import escolher_cor_borda, escolher_cor_preenchimento

janela = None
canvas = None
controlador = None

ferramenta = "retangulo"

cor_borda = "black"
cor_preenchimento = "white"


def selecionar_retangulo():
    global ferramenta
    ferramenta = "retangulo"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)


def selecionar_oval():
    global ferramenta
    ferramenta = "oval"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)


def selecionar_circulo():
    global ferramenta
    ferramenta = "circulo"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)


def selecionar_poligono():
    global ferramenta
    ferramenta = "poligono"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)


def selecionar_mao_livre():
    global ferramenta
    ferramenta = "mao_livre"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)


def selecionar_linha():
    global ferramenta
    ferramenta = "linha"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)


def selecionar_rabisco():
    global ferramenta
    ferramenta = "rabisco"
    if controlador is not None:
        controlador.selecionar_ferramenta(ferramenta)



def mudar_borda():
    global cor_borda
    cor_borda = escolher_cor_borda()


def mudar_preenchimento():
    global cor_preenchimento
    cor_preenchimento = escolher_cor_preenchimento()


def iniciar():
    global janela
    global canvas
    global controlador

    janela = tk.Tk()
    janela.title("Paint Orientado a Objeto")

    largura = 900
    altura = 600
    # Centraliza a janela na tela.
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela - largura) // 2
    pos_y = (altura_tela - altura) // 2
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    barra = tk.Frame(janela)
    barra.pack(fill="x")

 
    
    tk.Button(barra, text="Retângulo", command=selecionar_retangulo).pack(side="left")

    tk.Button(barra, text="Oval", command=selecionar_oval).pack(side="left")

    tk.Button(barra, text="Círculo", command=selecionar_circulo, ).pack(side="left")

    tk.Button(barra, text="Polígono", command=selecionar_poligono).pack(side="left")

    tk.Button(barra, text="Mão livre", command=selecionar_mao_livre).pack(side="left")

    tk.Button(barra, text="Linha", command=selecionar_linha).pack(side="left")

    tk.Button(barra, text="Rabisco", command=selecionar_rabisco).pack(side="left")

    tk.Button(barra, text="Cor da borda", command=mudar_borda).pack(side="left")

    tk.Button(barra, text="Cor preenchimento", command=mudar_preenchimento).pack(side="left")

    canvas = tk.Canvas(janela, bg="white")
    canvas.pack(fill="both", expand=True)

    controlador = ControladorDesenho(
        canvas,
        lambda: cor_borda,
        lambda: cor_preenchimento,
    )
    controlador.selecionar_ferramenta(ferramenta)

    # Liga os eventos do mouse para desenhar no canvas.
    canvas.bind("<Button-1>", controlador.clique)
    canvas.bind("<B1-Motion>", controlador.arrastar)
    canvas.bind("<ButtonRelease-1>", controlador.soltar)

    janela.mainloop()