""" O Rato no Labirinto - 1799
Author: Diego Mariano (@dcbmariano)

=== como testar localmente ===
Crie um arquivo chamado "entrada.txt" e coloque a entrada de exemplo dada no beecrowd. Em seguida, execute no terminal com:
python 1799.py < entrada.txt

=== Descrição do exercício === 
Em 1942, um estudo feito por Robert Tryon concluiu que os traços genéticos frequentemente podem contribuir para o comportamento, independente do meio ambiente. Para fazer isso Tryon criou uma experiência que testou a proficiência de gerações sucessivas de ratos em completar um labirinto, separando os que fizeram os menores números de erros em "brilhantes", e aqueles com mais erros em "medíocres". Dando continuidade a este processo durante sete gerações ele criou duas raças distintas de ratos: "brilhantes" e "medíocres".

O ratinho IBO é descendente da linhagem de ratos "brilhante", sendo o melhor de todos no desempenho deste experimento. Ele consegue entrar, pegar o queijo e sair de qualquer labirinto sem se perder, e sempre faz o caminho mais curto possível.

Sua tarefa neste problema é, dado o desenho do Labirinto e a posição do queijo, determinar por quantos pontos estrategicamente marcados por letras do alfabeto (ou palavras contendo somente letras) IBO deve passar para pegar o queijo (indicado pelo caractere '*') e sair, sempre partindo do ponto Entrada e terminando em Saida (sem acento). No exemplo abaixo, a sequência de IBO à partir da Entrada seria: A, F, J, *, I, M, K e Saida, o que resultaria em 8, que é a quantidade mínima de pontos pelos quais IBO deve passar para cumprir a sua tarefa. Se IBO tiver que passar por um ponto duas vezes (uma indo para o queijo e outra indo para a saída) isso conta como dois pontos visitados.

Entrada
A primeira linha de entrada contém dois inteiros Pontos (4 ≤ Pontos ≤ 4000) e Ligacoes (4 ≤ Ligacoes ≤ 5000) representando respectivamente o número de pontos estrategicamente marcados no labirinto e quantidade de ligações existentes entre estes pontos. Seguem as linhas que indicam cada uma das ligações entre estes pontos. As ligação entre dois pontos indica que qualquer um dos dois pode ser a origem.

Saída
Imprima um valor inteiro identificando a quantidade mínima de pontos do labirinto pelos quais IBO deve passar para cumprir a sua tarefa.
"""

import collections as c

visitado = [] 
fila = []    
la = {} # lista de adjacencias
dist={}
dist_ini = {}  # dicionario sera usado para armazenar as distancias ENTRADA=>QUEIJO
dist_fin = {}  # dist QUEIJO=>SAIDA


def bfs(grafo, visitado, vertice_origem, vertice_destino):
    """ realiza uma busca em largura """
    d=0 # distancia inicial é zero
    visitado.append(vertice_origem)
    fila = c.deque()
    fila.append(vertice_origem)

    if vertice_origem == "Entrada":
        dist_ini[vertice_origem] = 0
    else:
        dist_fin[vertice_origem] = 0
        
    while fila:
        atual = fila.popleft() # remove elemento atual e processa fila

        for vizinho in grafo[atual]:
            if vertice_origem == "Entrada":
                if dist_ini[vizinho] == float('inf'):
                    dist_ini[vizinho] = dist_ini[atual]+1
                    fila.append(vizinho)

                    if atual == 'queijo':  # melhora o processamento
                        return 0
            else:
                if dist_fin[vizinho] == float('inf'):
                    dist_fin[vizinho] = dist_fin[atual]+1
                    fila.append(vizinho)

                    if atual == 'Saida':  # melhora o processamento
                        return 0


def filtra(i):
    """ converte a entrada para lidar com caracteres especiais """
    if i == '*':
        return 'queijo'
    elif i == 'queijo':
        return '*'
    else:
        return i

# lê entrada de dados    
pontos, ligações = tuple([int(i) for i in input().split()]) # pega a primeira linha
pares = [tuple(map(filtra, input().split())) for _ in range(ligações)] 

# pegando os vertices unicos
for p in pares: 

    la[p[0]] = []
    la[p[1]] = []
    dist_ini[p[0]]=float('inf')
    dist_ini[p[1]]=float('inf')
    dist_fin[p[0]]=float('inf')
    dist_fin[p[1]]=float('inf')

for p in pares:  # preenche a lista de adjacências
    la[p[0]].append(p[1])
    la[p[1]].append(p[0])

# estrategia: calcula a distancia da entrada ao queijo
bfs(la, visitado, "Entrada", "queijo")
visitado = [] 
fila = []    
# estrategia: depois calcula a distancia do queijo a saida
distancia_queijo_saida = bfs(la, visitado, "queijo", "Saida")

print(dist_ini['queijo'] + dist_fin['Saida'])
