import heapq

def dijkstra(grafo, vertice_inicial, saida = None):
    """ Dijkstra: retorna o caminho mínimo de 1 para n vértices """

    n = len(grafo) # retorna tamanho do grafo
    distancias = {v: float('inf') for v in grafo}  # tood mundo começa com distâncias infinitas
    pai = {v: None for v in grafo}
    
    distancias[vertice_inicial] = 0  # a distância do item inicial é definida em 0
    
    fila = [(0, vertice_inicial)] # usando fila de prioridade (heap) para manter os vértices a serem explorados
    
    while fila:  # enquanto tiver elementos  na fila
        
        # pega vértice com a menor distância da fila de prioridade
        dist_atual, vertice_atual = heapq.heappop(fila) 
        
        if dist_atual > distancias[vertice_atual]: 
            continue # ignorar arestas com distâncias maiores que as já processadas
        
        # explorando os vizinhos do vértice atual
        for vizinho, peso in grafo[vertice_atual]:
            distancia = dist_atual + peso
            
            # RELAXAÇÃO: se a distância for menor, atualize o vetor de distâncias
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                pai[vizinho] = vertice_atual

                heapq.heappush(fila, (distancia, vizinho))
    
    if saida == 'distancias':
        return distancias   
    elif saida == 'predecessores':
        return pai
    elif saida == 'caminho':
        todos_caminhos = [caminho(pai, vertice_final = i) for i in grafo]
        return todos_caminhos
    else:
        return distancias, pai

def caminho(caminhos, vertice_final):

    caminho_atual = []
    v = vertice_final # comece do fim
    while v is not None:
        caminho_atual.insert(0, v)
        v = caminhos[v]

    return caminho_atual


grafo = {
    0: [(1, 1), (4, 1)], 
    1: [(0, 1), (2, 1), (3, 4)], 
    2: [(1, 1), (3, 2), (4, 5)], 
    3: [(1, 4), (2, 2), (4, 1)], 
    4: [(2, 5), (3, 1)]
}

dist_0_todos = dijkstra(grafo, vertice_inicial=0, saida='distancias')

for i in dist_0_todos:  # distancia do vértice 0 até todos os outros vértices
    print("Distância do vértice 0 até", i, "é de", dist_0_todos[i])

caminhos = dijkstra(grafo, vertice_inicial=0, saida='caminho')

for caminho in caminhos:
    print("\nCaminho de", caminho[0], "até", caminho[-1], "é:")
    for c in caminho:
        print(c, "=>", end=" ")
    print("dist:",len(caminho)-1)
