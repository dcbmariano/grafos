import time
inicio = time.time()

def Grafo(entrada):
    # entrada: vertices ou arestas
    return 0

def calcula_lista_de_adjacencias(pares, lista):
    
    lista[pares[0]].append(pares[1])
    lista[pares[1]].append(pares[0])


entrada = """4 3 2
0 1
1 2
2 3"""

grafo = {}
grafos = []

linhas = entrada.split("\n")

cont = 0
for i in range(1):
    for linha in linhas:
        cont+=1
        dados = linha.split()
        if len(dados) == 3:
            if cont!=1:
                grafos.append(grafo)

            grafo = {}
            grafo['vertices'] = int(dados[0])
            grafo['direcao'] = int(dados[2])
            grafo['arestas'] = []

            lista = {}
            for j in range(grafo['vertices']):
                lista[j] = []
            # print(lista)
        elif len(dados) == 2:
            dados[0] = int(dados[0]); dados[1] = int(dados[1])
            calcula_lista_de_adjacencias(dados, lista)

            grafo['arestas'].append(dados)

grafos.append(grafo) # adiciona último item
# print(lista)

print(grafos)
fim = time.time()

print(fim-inicio, 'segundos')

