# para testar use: python o_bom_presidente_v3.py < entrada.txt
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

lista_de_adjacencias = {} 
vertices = []

def ad_vertice(vertice):
    ''' Adiciona um vertice no grafo '''
    lista_de_adjacencias[vertice] = []

def ad_aresta(node1, node2):
    ''' Adiciona uma aresta no grafo '''
    temp = []  
    temp.extend(lista_de_adjacencias[node1])
    temp.append(node2) 
    lista_de_adjacencias[node1] = set(temp)

    temp = []  
    temp.extend(lista_de_adjacencias[node2])
    temp.append(node1)
    lista_de_adjacencias[node2] = set(temp)
       
def cria_grafo():
    ''' Fachada para criação de um novo grafo '''
    lista_de_adjacencias={}


# Aqui começa o programa ************************************************************

t = int(input())  # lê a primeira linha e pega quantos grafos tem no teste
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
        
        # para todo o vértice
        visitado = {}
        componente = {}
        qtd_componentes = 0

        # preenche tudo como vazio 
        for i in range(N):
            visitado[i] = 0
            componente[i] = -1

        # detectando componentes      
        for i in range(N): 
            if len(lista_de_adjacencias[i]) > 0: # analisa apenas vertices com arestas
                if visitado[i] == 0:
                    visitado[i] = 1
                    componente[i] = i
                    qtd_componentes += 1

                    visitados = busca_em_largura(lista_de_adjacencias, i)
                    for j in visitados:
                        visitado[j] = 1
                        componente[j] = i

        tamanho_componente = {}
        singleton = 0

        for i in componente:
            if componente[i] == -1:
                singleton+=1
            elif componente[i] not in tamanho_componente:
                tamanho_componente[componente[i]] = 1
            else:
                tamanho_componente[componente[i]] += 1
        
        # parte 1: custo parcial é num de clusters unicos por biblioteca 
        custo_total += singleton * custo_biblioteca

        # parte 2: custo parcial tbm deve ter custo de total de elementos -1 em um componente * estrada + custo de 1 biblioteca
        for i in tamanho_componente:
            custo_total += custo_biblioteca + ((tamanho_componente[i]-1) * custo_estrada)

    t-=1 
    print(custo_total)

# resultado esperado: [0] 805 [1] 184 [2] 80 [3] 5 [4] 204