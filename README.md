# Projeto de Programação A - 2026.1

Aplicação desenvolvida em Python utilizando Tkinter para criação de desenhos, inspirada em ferramentas como Google Drawings e LibreOffice Draw.

## Objetivo

Desenvolver um programa gráfico capaz de criar diferentes formas em uma área de desenho (canvas), aprimorando o projeto ao longo das entregas por meio de refatorações e da utilização de padrões de projeto.

## Tecnologias

* Python 3
* Tkinter
* Git e GitHub para controle de versões e desenvolvimento colaborativo

## Estrutura do Projeto

A aplicação adota o padrão **MVC (Model-View-Controller)** para separar responsabilidades e organizar a lógica do sistema em três camadas principais:

### models/ (Modelo)
Camada responsável pelas regras de negócio, estruturas de dados e representação dos elementos do sistema.

* **figuras.py:** Define a modelagem e o comportamento das figuras geométricas (Retângulo, Oval, Círculo, Linha, Rabisco, etc.).
* **desenho.py:** Gerencia o estado e o conjunto de desenhos armazenados no canvas.
* **cores.py:** Controla as definições e a aplicação das cores de borda e preenchimento das figuras.

### views/ (Visualização)
Camada encarregada de toda a interface gráfica e da apresentação visual para o usuário.

* **interface.py:** Renderiza a janela principal, organiza os componentes visuais e configura a área de desenho (canvas).

### controler/ (Controlador)
Camada intermediária que gerencia o fluxo de informações, capturando as ações do usuário na View e aplicando-as ao Model.

* **eventos.py:** Trata os eventos físicos do mouse (cliques e arrastes) para viabilizar as ações de desenho.
* **controlador.py:** Centraliza a lógica das ferramentas ativas e coordena a comunicação direta entre a View e o Model.

## Entrega 1 - imperativa.1

Nesta primeira etapa foi construída a versão funcional do programa seguindo o paradigma imperativo.

Funcionalidades implementadas:

* Criação de retângulos.
* Criação de ovais.
* Criação de círculos.
* Seleção da cor da borda para cada figura.
* Seleção da cor de preenchimento das figuras.
* Exibição de uma prévia da forma durante o arraste do mouse.

Aspectos da interface implementados:

* Janela exibida centralizada na tela.
* Barra de ferramentas contendo botões para selecionar formas e cores.

### Como executar

1. Abra a pasta do projeto pelo terminal.
2. Execute o comando:

```bash
python main.py
```

## Entrega 2 - OO.1

Nesta etapa foi realizada a refatoração do projeto para uma arquitetura baseada em orientação a objetos.

Funcionalidades implementadas nesta entrega:

* Criação de uma hierarquia de classes tendo **Figura** como classe principal.
* Implementação das subclasses para retângulo, oval, círculo, polígono regular e desenho à mão livre.
* Desenvolvimento de um controlador orientado a objetos responsável pela pré-visualização e pelo desenho definitivo no canvas.
* Organização das figuras em um módulo específico.
* Inclusão de novos recursos de desenho, como polígono e mão livre.

Organização obtida:

* Cada figura passou a ser responsável por desenhar sua própria prévia e sua versão definitiva.
* A interface ficou encarregada de montar a janela e encaminhar as ações ao controlador.
* O processo de desenho deixou de depender de diversas estruturas condicionais distribuídas pelo código.

## Entrega 3 - OO.MVC.1 

Nesta fase, o objetivo principal foi reorganizar a aplicação utilizando o padrão de arquitetura MVC.

Organização obtida:

* Criação classes de modelo responsáveis pelos dados e pelas figuras.
* Implementação da camada de visão encarregada da interface gráfica.
* Desenvolvimento de controladores para administrar a lógica de interação.
* Reorganização a estrutura do projeto, definindo melhor as responsabilidades de cada componente.
* Adição das funcionalidades de linha e rabisco.

## Entrega 4 - OO.State.1 (planejada)

Etapa prevista para substituir parte das estruturas condicionais pelo padrão State, além de adicionar funcionalidades para salvar e abrir desenhos.
