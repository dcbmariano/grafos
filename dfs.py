def dfs(grafo, inicio = 1, caminho = []):
    """ Retorna a busca em profundidade """
    visitados = set()
    pilha = [inicio]
    
    while pilha:
        vertice = pilha.pop()
        if vertice not in visitados:
            visitados.add(vertice)
            caminho.append(vertice)

            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    pilha.append(vizinho)
    
    return caminho

la = {
  1: [2, 5],
  2: [1, 3, 5],
  3: [2, 4],
  4: [3, 5, 6],
  5: [1, 2, 4],
  6: [4]
}

# print(la)
c = dfs(la, 1)
print(c)