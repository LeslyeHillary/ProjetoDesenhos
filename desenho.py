#Funções para desenhar
def desenhar_retangulo(canvas, x1, y1, x2, y2, borda, preenchimento):
    canvas.create_rectangle(
        x1, #coodernada do eixo x inicial
        y1, #coodernada do eixo y inicial
        x2, #coodernada do eixo x final
        y2, #coodernada do eixo y final
        outline=borda, #cor da borda
        fill=preenchimento # cor do preenchimento
    )


def desenhar_oval(canvas, x1, y1, x2, y2, borda, preenchimento):
    canvas.create_oval(
        x1, #coodernada do eixo x inicial
        y1, #coodernada do eixo y inicial
        x2, #coodernada do eixo x final
        y2, #coodernada do eixo y final
        outline=borda,
        fill=preenchimento
    )


def desenhar_circulo(canvas, x1, y1, x2, y2, borda, preenchimento):

    raio = min(abs(x2 - x1), abs(y2 - y1)) #calcula raio utilizando o menor deslocamento

    #ajusta a coodernada final do eixo x
    if x2 < x1: 
        x2 = x1 - raio
    else:
        x2 = x1 + raio

    #ajusta a coodernada final do eixo x
    if y2 < y1:
        y2 = y1 - raio
    else:
        y2 = y1 + raio

    canvas.create_oval(
        x1,
        y1,
        x2,
        y2,
        outline=borda,
        fill=preenchimento
    )