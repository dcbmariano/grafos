# O Bom Presidente by Diego Mariano
# Python é vida
# Fontes:
# https://www.programiz.com/dsa/graph-dfs
# https://www.pythonpool.com/adjacency-list-python/
# https://www.studytonight.com/python-howtos/how-to-add-a-list-to-a-set-in-python#:~:text=Whereas%2C%20sets%20in%20Python%20are,collection%20of%20distinct%20hashable%20objects.
# https://github.com/SamuelEduardoSilva/algoritmos/blob/master/Implementa%C3%A7%C3%B5es%20-%20Teoria%20dos%20Grafos/Implementa%C3%A7%C3%A3o%20BFS/BFS.cpp # me deu a dica de como ler os arquivos

debug = False

import collections
import random

def busca_em_largura(G, vertice_origem=0, mostrar_caminho=True, alvo=-1, mostrar_alvo=True):
    ''' busca em largura '''
    visitado, fila = set(), collections.deque([vertice_origem])
    visitado.add(vertice_origem)
    caminho = []

    if mostrar_alvo and alvo != -1:
        print("Alvo:", alvo)

    while fila:
        # Retira um vertice da fila
        vertice = fila.popleft()
        caminho.append(vertice)

        if mostrar_caminho:    
            if vertice == alvo:
                print(caminho)
                return caminho

        # Se não visitado, marca como visitado e enfilera
        for vizinho in G[vertice]:
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append(vizinho)

    if mostrar_caminho:
        print(caminho)
    else: 
        return caminho


def busca_em_profundidade(G, inicio=0, visitado=None, mostrar_caminho=True, alvo=-1, mostrar_alvo=True):
    ''' busca em profundidade '''
    if mostrar_caminho: 
        if mostrar_alvo and alvo != -1:
            print("Alvo:", alvo)

        if visitado != None:
            if inicio not in visitado:  # imprime o valor visitado
                print(inicio, end=" ")


    if visitado is None:
        visitado = set()
    visitado.add(inicio)

    try:
        for next in G[inicio] - visitado:
            if inicio == alvo:
                return
            busca_em_profundidade(G, next, visitado, alvo=alvo, mostrar_alvo=False)
    except:
        return

    return visitado

lista_de_adjacencias = {} # lista de adjacencia
vertices = []

def ad_vertice(vertice):
    lista_de_adjacencias[vertice] = []

 
def ad_aresta(node1, node2, bidirecional = True):
    temp = []  
    temp.extend(lista_de_adjacencias[node1])
    temp.append(node2) 
    lista_de_adjacencias[node1] = set(temp)

    if bidirecional:
        temp = []  
        temp.extend(lista_de_adjacencias[node2])
        temp.append(node1)
        lista_de_adjacencias[node2] = set(temp)
       

def Grafo():
    ''' imprime o grafo '''
    print("*** GRAFO ***")
    print("Vértice -> [Lista de adjacências]")
    for vertice in lista_de_adjacencias:
        print(vertice, " -> ", [i for i in lista_de_adjacencias[vertice]])
 
def cria_grafo():
    lista_de_adjacencias={}


# n = 96295 # 1000 vertices

# #adiciona vertices
# for i in range(n): 
#     ad_vertice(i)

#adiciona arestas
# for i in range(n//5): # 50 mil arestas
#     a = random.randint(0, n-1)
#     b = random.randint(0, n-1)

#     ad_aresta(a, b, False)
#['5', 
# '9 2 91 84', '8 2', '2 9', 
# '5 9 92 23', '2 1', '5 3', '5 1', '3 4', '3 1', '5 4', '4 1', '5 2', '4 2', 
# '8 3 10 55', '6 4', '3 2', '7 1', 
# '1 0 5 3', 
# '2 0 102 1']

# entrada = """2
# 3 3 2 1
# 1 2
# 3 1
# 2 3
# 6 6 2 5
# 1 3
# 3 4
# 2 4
# 1 2
# 2 3
# 5 6""".split("\n")

# caso d) 317186 linhas
# caso e) 194430 linhas 

entrada = """5
9 2 91 84
8 2
2 9
5 9 92 23
2 1
5 3
5 1
3 4
3 1
5 4
4 1
5 2
4 2
8 3 10 55
6 4
3 2
7 1
1 0 5 3
2 0 102 1""".split("\n") # resultado esperado: [0] 805 [1] 184 [2] 80 [3] 5 [4] 204

# # Lê entrada ******************************
# sair = False
# entrada = []
# while sair != True:
#     try:
#         linha = input()
#     except:
#         sair = True
#         continue
#     entrada.append(linha)
# # / fim lê entrada ************************


'''
N => NOS
M => ARESTAS

E => ESTRADA (CUSTO)
B => BIBLIOTECA (CUSTO)

T => MAPAS (TOTAL DE GRAFOS)
X Y => LINK ENTRE NOS X E Y

ENTRADA:
T
N M B E
X Y
'''
cont = 0
t = int(entrada[cont])  # t recebe o total de grafos
cont += 1 # próxima linha
while t > 0:  # enquanto houver grafos


    N, M, B, E = entrada[cont].split()

    # cria o grafo
    cria_grafo()

    # adiciona os vertices no grafo
    for j in range(int(N)):
        ad_vertice(j)

    if debug:
        print("Entrada:", N, M, B, E)
    M = int(M)  # M = arestas
    m = M
    while M > 0:  # enquanto houver arestas
        cont+=1  # próxima linha
        X, Y = entrada[cont].split()  # CIDADE X e Y
        X=int(X)-1; Y=int(Y)-1

        # adiciona as arestas no grafo
        ad_aresta(X, Y, True)

        M-=1

    cont += 1 # próxima linha

    t-=1 # próximo grafo

    #grafo = lista_de_adjacencias
    #print(grafo)

    N=int(N)
    vazio = 0
    custo_biblioteca = int(B)
    custo_estrada = int(E)
    custo_total = 0

    # CALCULANDO O CUSTO TOTAL 
    # > CASO 1: B <= E
    if int(B) <= int(E) or m == 0:
        if debug:
            print("Caso 1: N",N,"B",B, "M",M)
        custo_total = int(N) * int(B)

    # > CASO 2: B > E
    elif int(B) > int(E):
        # custo total = custo_singlegrafos + custo_subgrafos
        # determina os subgrafos
        subgrafos = []
        for i in range(N):
            if len(lista_de_adjacencias[i]) > 0:
                subgrafos.append(sorted(busca_em_largura(lista_de_adjacencias, i, mostrar_caminho=False)))
            else:
                vazio += 1
        # gambiarra suprema pra criar listas unicas
        subgrafos = [tuple(i) for i in subgrafos]
        subgrafos_unicos = set(subgrafos)

        #print("\nVértices vazios:", vazio)

        # custo_subgrafos = (n_subgrafos * custo_biblioteca + custo_estrada * elementos_em_subgrafos)

        n_subgrafos = len(subgrafos_unicos)
        elementos_em_subgrafos = 0

        for subgrafo in subgrafos_unicos:
            elementos_em_subgrafos += len(subgrafo)

        #print(n_subgrafos, custo_biblioteca, custo_estrada, elementos_em_subgrafos)
        custo_subgrafos = (n_subgrafos * custo_biblioteca) + (custo_estrada * (elementos_em_subgrafos - 1))

        # custo_singlegrafos = (custo_biblioteca * vazio) 
        custo_singlegrafos = custo_biblioteca * vazio

        # custo total = custo_singlegrafos + custo_subgrafos
        custo_total = custo_singlegrafos + custo_subgrafos

        if debug:
            print("Caso 2 => n_subgrafos:",n_subgrafos, 
                "/ elementos_em_subgrafos: ", elementos_em_subgrafos, 
                "/ custo single: ", custo_singlegrafos, 
                "/ custo_subgrafos:", custo_subgrafos,
                "/ vazio:", vazio, 
                "/ subgrafos:", subgrafos,
                "/ lista adjacências:", lista_de_adjacencias)

    print(custo_total)
