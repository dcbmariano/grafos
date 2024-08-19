""" Componentes Conexos - 1082
Author: Diego Mariano (@dcbmariano)

=== como testar localmente ===
Crie um arquivo chamado "entrada.txt" e coloque a entrada de exemplo dada no beecrowd:
--------------------------------------------------------------------------------
3
3 1
a c
10 10
a b
a c
a g
b c
c g
e d
d f
h i
i j
j h
6 4
a b
b c
c a
e f
--------------------------------------------------------------------------------

Em seguida, execute no terminal com:
python 1082.py < entrada.txt

=== Descrição do exercício === 
Com base nestas três definições:
- Grafo conexo: Um grafo G(V,A) é conexo se para cada par de nodos u e v existe um caminho entre u e v. Um grafo com apenas um componente é um grafo conexo.
- Grafo desconexo: Um grafo G(V,A) é desconexo se ele for formado por 2 ou mais componentes conexos.
- Componente conexo: Componentes conexos de um grafo são os subgrafos conexos deste grafo.

O grafo a seguir possui 3 componentes conexos. O primeiro é formado pelos nodos a,b,c. O segundo é formado unicamente pelo nodo d e o terceiro componente é formado pelos nodos e,f.


Com base nestes conceitos, onde cada entrada fornecida que tem a identificação de cada um dos vértices, arestas e as ligações entre os vértices através destas arestas,  liste cada um dos componentes conexos que existem no grafo, segundo a entrada fornecida.

Entrada
A primeira linha do arquivo de entrada contém um valor inteiro N que representa a quantidade de casos de teste que vem a seguir. Cada caso de teste contém dois valores V e E que são, respectivamente, a quantidade de Vértices e arestas (Edges) do grafo. Seguem E linhas na sequência, cada uma delas representando uma das arestas que ligam tais vértices. Cada vértice é representado por uma letra minúscula do alfabeto ('a'-'z'), ou seja, cada grafo pode ter no máximo 26 vértices. Cada grafo tem no mínimo 1 componente conexo.

Obs: Os vértices de cada caso de teste sempre iniciam no 'a'. Isso significa que um caso de teste que tem 3 vértices, tem obrigatoriamente os vértices 'a', 'b' e 'c'.

Saída
Para cada caso de teste da entrada, deve ser apresentada uma mensagem Case #n:, onde n indica o número do caso de teste (conforme exemplo abaixo). Segue a listagem dos vértices de cada segmento, um segmento por linha, separados por vírgula (inclusive com uma virgula no final da linha). Finalizando o caso de teste, deve ser apresentada uma mensagem indicando a quantidade de componentes conexos do grafo (em inglês). Todo caso de teste deve ter uma linha em branco no final, inclusive o último caso de teste.

Obs: os nodos devem sempre ser apresentados em ordem crescente e se há caminho de a até b significa que há caminho de b até a."""


def dfs(grafo, visitado, visitado_all, vertice): 
    """ função que realiza uma busca em profundidade """
    if vertice not in visitado:
        # print(vertice, end=",")
        global saida
        saida.add(vertice)
        visitado.add(vertice)
        visitado_all.add(vertice)
        
        for vizinho in grafo[vertice]:
            dfs(grafo, visitado, visitado_all, vizinho)


n = int(input()) # pega a primeira linha
caso = 0
saida = set()

while n > 0:
    cc = 0 # componentes conectados
    caso += 1 # imprime cada grafo avaliado
    v, e = map(int, input().split())  # pega os vértices e as arestas

    pares = [] # cria uma lista para receber todos os pares de vértices
    la = {} # lista de adjacencias

    pares = [tuple(input().split()) for _ in range(e)]  #ord retorna o código ascii da letra (chr pra converter de volta)
    
    for i in range(v):  # inicializa lista de adjacencias vazia
        la[chr(97+i)] = []

    for p in pares:  # preenche a lista de adjacências
        la[p[0]].append(p[1])
        la[p[1]].append(p[0])

    print("Case #", caso, ":", sep="")
    visitado_all = set()  # pequena gambiarra para armazenar todos os visitados

    for i in range(v): # para cada vertice
        #dfs para os outros
        i = chr(97+i)
        saida = set()
        if i not in visitado_all:
            visitado = set()  # cria um conjunto vazio para armazenar visitados
            
            dfs(la, visitado, visitado_all, i)  # na tabela ascii, o caractere a=97, b=98, c=99, []...] 
            saida = list(saida)
            saida.sort()
            for i in saida:
                print(i+',', end='')
            print() # imprime linha em branco
            cc+=1  # incrementa os componentes conectados
    
    print(cc, "connected components\n")  # imprime a quantidade de componentes conectados

    n -= 1
