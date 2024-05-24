def dfs(grafo, inicio = 1, caminho = []):
    """ Retorna a busca em profundidade """
    visitados = set()
    pilha = [(inicio, 'entrada')]
    tempo = 0
    
    while pilha:
        vertice, operacao = pilha.pop()

        if operacao == 'entrada':
            if vertice not in visitados:
                visitados.add(vertice)
                caminho.append(vertice)

                tempo += 1
                ot[vertice]["inicio"] = tempo
                pilha.append((vertice, 'saida')) # registrar saida

                for vizinho in grafo[vertice]:
                    if vizinho not in visitados:
                        pilha.append((vizinho, 'entrada'))
        elif operacao == 'saida':
            tempo += 1
            ot[vertice]["fim"] = tempo
    
    return caminho

# lista de adjacências
la = {
  1: [2, 5],
  2: [1, 3, 5],
  3: [2, 4],
  4: [3, 5, 6],
  5: [1, 2, 4],
  6: [4]
}

# ordenação topológica
ot = { i: {"inicio": -1, "fim": -1} for i in la}

# print(la)
c = dfs(la, 1)
print(c)  # caminho
print(ot) # ordenação topológica