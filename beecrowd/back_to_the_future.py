# '''
# n ≥ 2 and n ≤ 100 (cidades)
# m ≥ 1 and m ≤ 5000 (rotas)
# a b c = rota de a até b + c (preço)
# d k = d são os amigos e k são os assentos livres
# '''

# entrada = """4 5
# 1 4 1
# 1 3 3
# 3 4 4
# 1 2 2
# 2 4 5
# 20 10
# 4 4
# 1 3 3
# 3 4 4
# 1 2 2
# 2 4 5
# 20 100
# 4 4
# 1 3 3
# 3 4 4
# 1 2 2
# 2 4 5
# 20 1""".split('\n')

from collections import deque

# Função que retorna os componentes conexos que contém pelo menos uma biblioteca
def find_connected_components(graph, libraries):
    visited = [False] * (len(graph) + 1)
    connected_components = []

    # Percorre o grafo a partir de cada cidade que já tem uma biblioteca
    for library in libraries:
        if not visited[library]:
            connected = set()
            queue = deque([library])
            visited[library] = True

            # Busca em largura
            while queue:
                current = queue.popleft()
                connected.add(current)

                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True

            connected_components.append(connected)

    return connected_components

# Função que calcula o custo mínimo para reconstruir o país
def calculate_cost(n, m, b, e, edges):
    # Cria o grafo a partir das estradas obstruídas
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Encontra os componentes conexos que contém pelo menos uma biblioteca
    libraries = set()
    for i in range(1, n + 1):
        if graph[i]:
            libraries.add(i)
    connected_components = find_connected_components(graph, libraries)

    # Calcula o custo de construir bibliotecas em cada componente conexo
    total_cost = 0
    for component in connected_components:
        if len(component) == 1:
            total_cost += b
        else:
            total_cost += min(b + e * (len(component) - 1), e * (len(component) - 1) + b)

    return total_cost

# Leitura da entrada
t = 2

dados = """1 4 1
1 3 3
3 4 4
1 2 2
2 4 5""".split("\n")

for _ in range(t):
    n, m, b, e = map(int, "4 5 20 10".split())
    edges = [tuple(map(int, dados[_].split())) for _ in range(m)]

    # Cálculo do custo mínimo para reconstruir o país
    cost = calculate_cost(n, m, b, e, edges)

    # Saída
    print(cost)