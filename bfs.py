from collections import deque

def bfs(grafo, inicio, caminho = []):
    """ Busca em profundidade """
    visitados = set()  
    fila = deque([inicio])  
    niveis = { i:-1 for i in grafo}
    niveis[inicio] = 0

    while fila:
        vertice = fila.popleft()  
        if vertice not in visitados:
            visitados.add(vertice)
            caminho.append(vertice)
            
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    fila.append(vizinho)
                    niveis[vizinho] = niveis[vertice]+1

    return caminho, niveis

la = {
  1: [2, 5],
  2: [1, 3, 5],
  3: [2, 4],
  4: [3, 5, 6],
  5: [1, 2, 4],
  6: [4]
}

# print(la)
c,d = bfs(la, 1)
print(c)  # caminho
print(d)  # distancias

