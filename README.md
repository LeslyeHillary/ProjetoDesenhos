# Projeto de Programação A - 2026.1

Aplicação desenvolvida em Python utilizando Tkinter para criação de desenhos, inspirada em ferramentas como Google Drawings e LibreOffice Draw.

## Objetivo

Desenvolver um programa gráfico capaz de criar diferentes formas em uma área de desenho (canvas), aprimorando o projeto ao longo das entregas por meio de refatorações e da utilização de padrões de projeto.

## Tecnologias

* Python 3
* Tkinter
* Git e GitHub para controle de versões e desenvolvimento colaborativo

## Estrutura atual do projeto

* **main.py:** arquivo responsável por iniciar a aplicação.
* **interface.py:** cria a janela principal, a barra de ferramentas, o canvas e conecta o controlador responsável pelos desenhos.
* **eventos.py:** reúne o controlador orientado a objetos que gerencia os eventos de clique, arraste e liberação do mouse.
* **figuras.py:** contém a classe base **Figura** e suas subclasses para retângulo, oval, círculo, polígono e desenho à mão livre.
* **desenho.py:** mantém as funções da versão anterior do sistema para fins de histórico.
* **cores.py:** realiza a escolha das cores da borda e do preenchimento utilizando a paleta padrão do sistema.

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

## Entrega 3 - OO.MVC.1 (visão geral)

Nesta fase, o objetivo principal foi reorganizar a aplicação utilizando o padrão de arquitetura MVC.

Planejamento geral:

* Criar classes de modelo responsáveis pelos dados e pelas figuras.
* Implementar a camada de visão encarregada da interface gráfica.
* Desenvolver controladores para administrar a lógica de interação.
* Reorganizar a estrutura do projeto, definindo melhor as responsabilidades de cada componente.

## Entrega 4 - OO.State.1 (planejada)

Etapa prevista para substituir parte das estruturas condicionais pelo padrão State, além de adicionar funcionalidades para salvar e abrir desenhos.
