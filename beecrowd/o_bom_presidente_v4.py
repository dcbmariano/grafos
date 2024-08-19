from sys import stdin  # isso melhora a performance
import collections

def busca_em_largura(G, vertice_origem=0):
    ''' Realiza um BFS no grafo G '''
    visitado, fila = set(), collections.deque([vertice_origem])
    visitado.add(vertice_origem)
    caminho = []

    while fila:
        vertice = fila.popleft()
        caminho.append(vertice)

        for vizinho in G[vertice]:
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append(vizinho)

    return caminho

def ad_vertice(vertice):
    ''' Adiciona um vertice no grafo '''
    lista_de_adjacencias[vertice] = set()

def ad_aresta(node1, node2):
    ''' Adiciona uma aresta no grafo '''
    lista_de_adjacencias[node1].add(node2)
    lista_de_adjacencias[node2].add(node1)
       
def cria_grafo():
    ''' Fachada para criação de um novo grafo '''
    lista_de_adjacencias={}


def grafo_vazio(n):
    anterior = list(range(n))
    visitado = [0]*n
    return anterior,visitado

def busca_componente(x, anterior):
    if x != anterior[x]:
        anterior[x] = busca_componente(anterior[x], anterior)
    return anterior[x]

def analisa_arestas(x, y, anterior, visitado):
    x2 = busca_componente(x,anterior)
    y2 = busca_componente(y,anterior)
    if x2 != y2: # se x2 é diferente de y2
        if visitado[x2] > visitado[y2]:
            anterior[y2] = x2
        else:
            anterior[x2] = y2
            if visitado[x2] == visitado[y2]:
                visitado[y2] += 1

# Aqui começa o programa ************************************************************

t = int(stdin.readline()) # lê a primeira linha e pega quantos grafos tem no teste

for _ in range(t): 
    N, M, B, E = map(int, stdin.readline().split())
    # cria_grafo() # perfornce lenta 
    # N, M, B, E = input().split()
    # cria_grafo()
    # for j in range(int(N)):
    #     ad_vertice(j)
    vertices = [tuple(map(int, stdin.readline().split())) for _ in range(M)] # deste modo é mais rápido
    anterior,visitado = grafo_vazio(N)
    # M = int(M); N=int(N)
    # m = M
    # while M > 0:
    #     X, Y = input().split() 
    #     X=int(X)-1; Y=int(Y)-1
    #     ad_aresta(X, Y)
    #     M-=1

    # vazio = 0
    # custo_biblioteca = int(B)
    # custo_estrada = int(E)
    # custo_total = 0
    
    for x,y in vertices:
        analisa_arestas(x-1,y-1,anterior,visitado)

    # caso 1: mais simples
    if B <= E or M == 0:
        print(N * B)
        continue

    # calculando componentes
    arvore = {busca_componente(i, anterior) for i in range(N)}
    total_componentes = len(arvore)

    # caso 2: custo de biblioteca x sigletons + total de componentes * b
    singletons = N-total_componentes
    custo_total = (singletons * E)+(total_componentes * B)

    #t-=1 
    print(custo_total)