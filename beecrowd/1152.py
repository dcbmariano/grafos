"""Estradas Escuras 1152
Author: Diego Mariano (@dcbmariano)

=== como testar localmente ===
Crie um arquivo chamado "entrada.txt" e coloque a entrada de exemplo dada no beecrowd. Em seguida, execute no terminal com:
python 1152.py < entrada.txt

=== Descrição do exercício === 
Nestes dias se pensa muito em economia, mesmo em Byteland. Para reduzir custos operacionais, o governo de Byteland decidiu otimizar a iluminação das estradas. Até agora, todas as rotas eram iluminadas durante toda noite, o que custava 1 Dólar Byteland por metro a cada dia. Para economizar, eles decidiram não iluminar mais todas as estradas e desligar a iluminação de algumas delas. Para ter certeza que os habitantes de Byteland continuem a se sentirem seguros, eles querem otimizar o sistema de tal forma que após desligar a iluminação de algumas estradas à noite, sempre existirá algum caminho iluminado de qualquer junção de Byteland para qualquer outra junção.

Qual é a quantidade máxima de dinheiro que o governo de Byteland pode economizar, sem fazer os seus habitantes sentirem-se inseguros?

Entrada
A entrada contém vários casos de teste. Cada caso de teste inicia com dois números m (1 ≤ m ≤ 200000) e n (m-1 ≤ n ≤ 200000), que são o número de junções de Byteland e o número de estradas em Byteland, respectivamente. Seguem n conjuntos de três valores inteiros, x, y e z, especificando qual será a estrada bidirecional entre x e y com z metros (0 ≤ x, y < m e x ≠ y).

A entrada termina com m=n=0. O grafo especificado em cada caso de teste é conectado. O tamanho total de todas as estradas em cada caso de teste é menor do que 231.

Saída
Para cada caso de teste imprima uma linha contendo a máxima quantidade diária de dólares de Byteland que o governo pode economizar.
"""

# por algum motivo o exercício inverte m com n (neste caso, m são vértice e n arestas)
m, n = map(int, input().split()) # executa pelo menos 1x

def busca(v, pai):
    """ busca o 'pai' de um vertice """
    if pai[v] == v:
        return v  # condição de parada
    # caso ache, repita a busca
    return busca(pai[v], pai)

def juntar(x, y, rank, pai):
    """ permite juntar subconjuntos """
    v1 = busca(x, pai)
    v2 = busca(y, pai)

    if v1 != v2: # se vertice raiz 1 for diferente de v2
        if rank[v1] > rank[v2]:
            pai[v2] = v1
        elif rank[v1] < rank[v2]: 
            pai[v1] = v2
        else:
            rank[v1] += 1
            pai[v2] = v1
    # print(rank)

def kruskal(pares, m, n):
    """ implementação do algoritmo de kruskal para encontrar a árvore geradora mínima"""
    agm = [] # arvore geradora minima
    # print(pares) #antes
    pares.sort(key=lambda x: x[2]) # Ordena arestas por peso (ordem crescente)
    # print(pares) #depois

    pai = [i for i in range(m)]  # cada aresta sera pai de si propria inicialmente
    rank = m*[0]  # cria um rank para armazenar 

    for x, y, z in pares:
        # xy (arestas) / z (peso)
        if busca(x, pai) != busca(y, pai):
            agm.append((x, y, z))  # adiciona aresta a arvore mínima
            juntar(x, y, rank, pai)  # une subconjuntos

    return agm

def processa(m, n):
    pares = [tuple(map(int,input().split())) for _ in range(n)]

    # Lista de adjacências parece desnecessária =======!
    # la = {} # lista de adjacencias
    # for i in range(m):  # inicializa lista de adjacencias vazia
    #     la[i] = []
    # for p in pares:  # preenche a lista de adjacências
    #     la[p[0]].append((p[1],p[2])) # [vertice]=>(vizinho, peso)
    #     la[p[1]].append((p[0],p[2])) 
    
    # calcula a árvore geradora mínima
    mst = kruskal(pares, m, n)

    # custo do caminho minimo
    custo = 0
    for i in mst:
        custo+=i[2]

    # custo de deixar todas as luzes acesas
    custo_total = 0
    for i in pares:
        custo_total += i[2]

    economia = custo_total-custo
    print(economia)


# do while
while m != 0 and n != 0:  # para quando m,n=0
    processa(m, n)
    m, n = map(int, input().split()) 
