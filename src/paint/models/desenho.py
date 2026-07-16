class Desenho: #Classe responsável por armazenar todas as figuras criadas, funciona como o modelo (Model) da aplicação MVC.


    def __init__(self): # Lista onde serão armazenadas todas as figuras desenhadas
        self.figuras = []


    def adicionar_figura(self, figura): #Adiciona uma nova figura à lista de desenhos.
        self.figuras.append(figura)


    def remover_figura(self, figura): #Remove uma figura da lista, caso ela exista.
        if figura in self.figuras:
            self.figuras.remove(figura)


    def limpar(self): #Remove todas as figuras armazenadas, deixando o desenho vazio.
        self.figuras.clear()