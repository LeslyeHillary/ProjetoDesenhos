from desenho import desenhar_retangulo
from desenho import desenhar_oval
from desenho import desenhar_circulo
import interface

x_inicial = 0 #marca onde o desenho começa na coodernada x
y_inicial = 0 #marca onde o desenho começa na coordernada y

preview = None

#executa quando o usuario clica
def clique(evento):
    global x_inicial
    global y_inicial

    x_inicial = evento.x
    y_inicial = evento.y


def arrastar(evento):
    global preview #permite modificar a variavel preview

    if preview is not None:
        interface.canvas.delete(preview)

    if interface.ferramenta == "retangulo": #verifica se foi selecionado a opção retangulo
        #cria um retangulo temporario
        preview = interface.canvas.create_rectangle(
            x_inicial,
            y_inicial,
            evento.x,
            evento.y,
            outline=interface.cor_borda,
            fill=interface.cor_preenchimento,
            stipple="gray50", #deixa o preenchimento transparente
            dash=(4, 2) #faz a borda ficar tracejada
        ) 

    elif interface.ferramenta == "oval": #caso a ferramenta seja oval
        #cria um oval temporario
        preview = interface.canvas.create_oval(
            x_inicial,
            y_inicial,
            evento.x,
            evento.y,
            outline=interface.cor_borda,
            fill=interface.cor_preenchimento,
            stipple="gray50",
            dash=(4, 2)
        )

    elif interface.ferramenta == "circulo": #caso a ferramenta escolhida seja um circulo
        raio = min(abs(evento.x - x_inicial), abs(evento.y - y_inicial)) #calcula o menor deslocamento

        if evento.x < x_inicial: #define posição dinal no eixo x
            x_final = x_inicial - raio
        else:
            x_final = x_inicial + raio

        if evento.y < y_inicial: #define posição final eixo y
            y_final = y_inicial - raio
        else:
            y_final = y_inicial + raio

        preview = interface.canvas.create_oval(
            x_inicial,
            y_inicial,
            x_final,
            y_final,
            outline=interface.cor_borda,
            fill=interface.cor_preenchimento,
            stipple="gray50",
            dash=(4, 2)
        )


def soltar(evento): #executa quando o usario soltar o botao do mouse
    global preview

    if preview is not None:
        interface.canvas.delete(preview)
        preview = None

    if interface.ferramenta == "retangulo": #caso seja um retangulo
        desenhar_retangulo(
            interface.canvas,
            x_inicial,
            y_inicial,
            evento.x,
            evento.y,
            interface.cor_borda,
            interface.cor_preenchimento
        )

    elif interface.ferramenta == "oval": #caso seja um oval
        desenhar_oval(
            interface.canvas,
            x_inicial,
            y_inicial,
            evento.x,
            evento.y,
            interface.cor_borda,
            interface.cor_preenchimento
        )

    elif interface.ferramenta == "circulo": #caso seja um circulo
        desenhar_circulo(
            interface.canvas,
            x_inicial,
            y_inicial,
            evento.x,
            evento.y,
            interface.cor_borda,
            interface.cor_preenchimento
        )