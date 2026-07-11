from tkinter.colorchooser import askcolor

# Abre a janela para o usuário escolher a cor da borda
def escolher_cor_borda():
    cor = askcolor()[1]

    # Se o usuário cancelar, usa preto como cor padrão
    if cor is None:
        return "black"

    return cor

# Abre a janela para o usuário escolher uma cor de preenchimento
def escolher_cor_preenchimento():
    cor = askcolor()[1]

    # Se o usuário cancelar, usa branco como cor padrão
    if cor is None:
        return "white"

    return cor