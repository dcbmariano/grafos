import math

print("Implementação do dijkstra em Python")

def inicializar_fonte_unica(grafo, s):
    n = len(grafo)
    distancias = [math.inf] * n
    pais = [None] * n
    for v in range(n):
        distancias[v] = float("+infinity")
        pais[v] = None
    distancias[s] = 0
    return distancias, pais

def extrair_minimo(Q, S):
    n = len(Q)
    minimo = None
    for v in range(n):
        if not S[v]:
            if minimo == None:
                minimo = v
            elif Q[v] < Q[minimo]:
                minimo = v
    return minimo

def dijkstra(grafo, s):
    distancias, pais = inicializar_fonte_unica(grafo, s)
    n = len(grafo)
    S = [False] * n
    Q = distancias
    for i in range(n):
        u = extrair_minimo(Q, S)
        S[u] = True
        for peso, v in grafo[u]:
            if distancias[v] > distancias[u] + peso:
                distancias[v] = distancias[u] + peso
                pais[v] = u
    return distancias, pais

def iniciar():
    grafo = [
        [(10, 1), (5, 3)],
        [(1, 2), (2, 3)],
        [(4, 4)],
        [(3, 1), (9, 2), (2, 4)],
        [(7, 0), (6, 2)]
    ]

    distancias, pais = dijkstra(grafo, 0)

    assert distancias == [0, 8, 9, 5, 7]
    print("Distâncias =", distancias)

    assert pais == [None, 3, 1, 0, 3]
    print("Pais =", pais)

iniciar()