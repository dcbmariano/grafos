import collections

def busca_em_largura(G, vertice_origem=0):
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

lista_de_adjacencias = {} 
vertices = []

def ad_vertice(vertice):
    lista_de_adjacencias[vertice] = []

def ad_aresta(node1, node2):
    temp = []  
    temp.extend(lista_de_adjacencias[node1])
    temp.append(node2) 
    lista_de_adjacencias[node1] = set(temp)

    temp = []  
    temp.extend(lista_de_adjacencias[node2])
    temp.append(node1)
    lista_de_adjacencias[node2] = set(temp)
       
def cria_grafo():
    lista_de_adjacencias={}

t = int(input())  
while t > 0:  
   
    N, M, B, E = input().split()
    cria_grafo()
    for j in range(int(N)):
        ad_vertice(j)

    M = int(M); N=int(N)
    m = M
    while M > 0:
        X, Y = input().split() 
        X=int(X)-1; Y=int(Y)-1
        ad_aresta(X, Y)
        M-=1

    vazio = 0
    custo_biblioteca = int(B)
    custo_estrada = int(E)
    custo_total = 0
 
    if int(B) <= int(E) or m == 0:
        custo_total = int(N) * int(B)
    elif int(B) > int(E):
        subgrafos = []
        for i in range(N):
            if len(lista_de_adjacencias[i]) > 0:
                subgrafos.append(sorted(busca_em_largura(lista_de_adjacencias, i)))
            else:
                vazio += 1
        subgrafos = [tuple(i) for i in subgrafos]
        subgrafos_unicos = set(subgrafos)
        n_subgrafos = len(subgrafos_unicos)
        elementos_em_subgrafos = 0
        for subgrafo in subgrafos_unicos:
            elementos_em_subgrafos += len(subgrafo)
        custo_subgrafos = (n_subgrafos * custo_biblioteca) + (custo_estrada * (elementos_em_subgrafos - 1))
        custo_singlegrafos = custo_biblioteca * vazio
        custo_total = custo_singlegrafos + custo_subgrafos

    t-=1 
    print(custo_total)
