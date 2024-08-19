"""Back to the Future - 1447
por Diego Mariano (@dcbmariano)

=== como testar localmente ===
Crie um arquivo chamado "entrada.txt" e coloque a entrada de exemplo dada no beecrowd. Em seguida, execute no terminal com:
python 1447.py < entrada.txt

=== Descrição do exercício === 
Um grupo de amigos resolveu ir à Alemanha para apoiar a seleção brasileira em sua jornada gloriosa rumo ao hexa. Como as passagens aéreas e as estadias eram caras, cada um trouxe uma quantidade de dinheiro que julgou suﬁciente para passar o mês com conforto e voltar para casa sem problemas.

Porém, após a bela campanha do Brasil na copa do mundo, o grupo de amigos se viu obrigado a gastar o dinheiro que tinha guardado para as etapas ﬁnais da copa com a famosa cerveja alemã. As consequências de tais atos foram terríveis. Após uma grande bebedeira, todos foram pegos pela polícia local dormindo na rua, e receberam multas pesadíssimas. Além disso, todos perderam suas passagens de volta. Devido a esses contratempos, a viagem de volta ﬁcou ameaçada. De repente, eles descobriram que precisavam voltar para casa gastando a menor quantidade possível de dinheiro.

Analisando as rotas aéreas disponíveis, os amigos notaram que em todas as rotas o número de assentos disponíveis nos aviões era sempre o mesmo. Porém, os preços das viagens entre uma cidade e outra eventualmente variavam bastante. Assustados com a possibilidade de não encontrar lugares suﬁciente nos aviões para que todos pudessem voltar e preocupados em gastar a menor quantidade possível de dinheiro, o grupo de amigos resolveu pedir sua ajuda.

Entrada
O problema é composto por várias instâncias. Cada instância começa com uma linha com dois inteiros positivos N (2 ≤ N ≤ 100) e M (1 ≤ M ≤ 5000), onde N é o número de cidades que pertencem às M rotas de voo consideradas. Os amigos querem ir da cidade 1 até a cidade N.

Nas próximas M linhas são fornecidos triplas de inteiros A B C descrevendo a rota do avião (A e B) e o preço da passagem aérea por pessoa (C). Os valores de A e B estão entre 1 e n. As rotas são bidirecionais (ou seja, há um voo de A até B e um voo de B até A com preço C) e haverá no máximo uma rota entre duas cidades. Na próxima linha são dados dois inteiros, D e K, onde D é o número de amigos e K é o número de assentos livres em cada voo. Cada rota só pode ser utilizada uma vez.

Saída
Para cada instância, imprima a linha "Instancia k", onde k é o número da instância atual. Além disso, imprima a menor quantidade possível de dinheiro que os amigos vão gastar para voltar ao Brasil (que está limitada por 1015). Caso não seja possível escolher um conjunto de voos que levem todos para casa, imprima "impossivel".

Imprima uma linha em branco após cada instância.
"""

import heapq

n_max = 100  # indicado na descrição do problema  N (2 ≤ N ≤ 100)
n_max += 1  # corrige um bug 

n, k, m, custo, d, instancia = 0, 0, 0, 0, 0, 0  # variáveis globais
capacidade = [[0 for _ in range(n_max)] for _ in range(n_max)]  # define a capacidade das arestas
distancia = [float('inf')] * n_max  # lista auxiliar com as dist (inicia com infinito)
anterior = [-1]*n_max  # armazena o vertice anterior
la = [[] for _ in range(n_max)]  # lista de adjacências começa vazia

def dijkstra():
    """ Algoritmo de caminho mínimo de Dijkstra usando heapq """
    global instancia, d, n, k, m, custo  #variáveis globais

    fila = [(0, 1)]
    heapq.heapify(fila)
    
    #for i in range(n): 
    for i in range(1, n+1):  # mudar tudo para 1 até n+1
        distancia[i] = float('inf') # dist começa com infinito
        anterior[i] = -1 # anterior começa com -1
    distancia[1] = 0 # primeiro vertice tem dist = 0

    # enquanto tiver elementos na fila
    while fila:
        
        # pega vértice com a menor distância da fila de prioridade
        dist_atual, vertice_atual = heapq.heappop(fila)

        if dist_atual > distancia[vertice_atual]:
            continue  # ignorar arestas com distâncias maiores que as já processadas

        if vertice_atual == n:
            break  # para a execução
        
        # para cada vizinho do vertice atual: aplica relaxação
        relax(vertice_atual, dist_atual, fila) #cada aresta deve ser relaxada 
    
    if distancia[n] == float('inf'): # se nao tem caminho, sai
        return False
    
    caminho = [n]
    atual = n

    # agora vamos preencher o caminho
    while atual != 1:
        parte_caminho = anterior[atual]
        caminho.append(parte_caminho)
        atual = parte_caminho
    
    #faz o caminho reverso
    caminho.reverse()
    #print(caminho)
    tmp = d  # variavel auxiliar

    for i in range(len(caminho)-1):
        tmp2 = capacidade[caminho[i]][caminho[i+1]]
        tmp = min(tmp, tmp2)
    
    d -= tmp
    tamanho_caminho = len(caminho)
    for i in range(tamanho_caminho - 1):
        prox_i = i+1 # proximo valor
        capacidade[caminho[i]][caminho[prox_i]] -= tmp
        capacidade[caminho[prox_i]][caminho[i]] += tmp
    #print('aqui')
    return True


def relax(vertice_atual, dist_atual, fila):
    """ RELAXAÇÃO: se a distância for menor, atualize o vetor de distâncias e capacidades """

    # para cada vizinho do vertice atual
    for vizinho, peso in la[vertice_atual]: 
        # se a capacidade [viz] até o vert atual menor q k
        if capacidade[vizinho][vertice_atual] < k:
            peso *= -1 #volta a -1
        if dist_atual + peso < distancia[vizinho] and capacidade[vertice_atual][vizinho] > 0:
            distancia[vizinho] = dist_atual + peso  # atualiza distancia
            anterior[vizinho] = vertice_atual  #atualiza o anterior do vizinho para o vertice atual
            heapq.heappush(fila, (distancia[vizinho], vizinho)) #adiciona na fila


def le_dados():
    """ Função que lê a entrada de dados """

    global instancia, d, n, k, m, custo  # variáveis globais

    try:  # tenta ler a linha
        n, m = map(int, input().split())
    except:  # se falhar, finaliza a execução
        return False
    
    
    #for i in range(n):
    for i in range(1, n + 1):
        la[i] = []
        #for j in range(n):
        for j in range(1, n + 1):
            capacidade[i][j] = 0
    
    custo = 0 # reseta custo

    # preenche a lista de adjacências
    for _ in range(m):
        #triplas de inteiros A B C descrevendo a rota do avião (A e B) e o preço da passagem aérea por pessoa (C)
        a, b, c = map(int, input().split())  # a = vert 1. b = vert 2. c = peso

        # atualiza lista de adjacencias
        la[a].append((b, c))
        la[b].append((a, c)) # aresta ida e volta

        # preenche a capacidade
        capacidade[a][b] = 1 # capacidade começa com 1
        capacidade[b][a] = 1

    # D e K, onde D é o número de amigos e K é o número de assentos livres em cada voo
    d, k = map(int, input().split())

    # atualiza a capacidade como proporcional a k
    #for i in range(n):
    for i in range(1, n + 1):
        #for j in range(n):
        for j in range(1, n + 1):
            capacidade[i][j] *= k
    
    # para cada caminho
    while dijkstra():
        if d <= 0:
            break 
    
    # calculo de custo
    #for i in range(n):
    for i in range(1, n + 1):
        for j in range(len(la[i])):
            v = la[i][j][0]
            if capacidade[i][v] < k: # se a capacidade atual for menor q k
                custo += la[i][j][1] * (k - capacidade[i][v])
    
    # ================== imprime saída na tela ==================
    print("Instancia",instancia+1)
    if d == 0:
        print(custo, "\n", sep="")
    else:
        print("impossivel", "\n", sep="")

    instancia += 1
    
    le_dados()  # recursiva


# inicia a execução
le_dados()