# -*- coding: utf-8 -*-
total_grafos = -1
grafos = []
sair = False
cont = 0

while sair != True:
  cont += 1
  #if cont > 3800:
  #  sair = True
  linha = input()
    
  i = linha.split()
  if len(i) == 2:
    total_grafos+=1
    grafos.append({
      "grafo":total_grafos,
      "vertices":i[0],
      "arestas":i[1],
      "links":[]
    })
  elif len(i) == 3:
    grafos[total_grafos]["links"].append(linha)
  if int(i[0]) == 0:
    sair = True

def busca_em_profundidade(g, visitado, v):
  n = len(g)
  visitado[v] = True
  for i in range(n):
    if g[v][i] == 1 and not visitado[i]:
      # chama a função recursivamente
      busca_em_profundidade(g, visitado, i)

def verifica_conexao(g):
  n = len(g)
  visitado = [False] * n
  # realiza uma busca e profundidade
  busca_em_profundidade(g, visitado, 0)

  return all(visitado)

def imprime_saida(saida):
  if saida == True:
    print(1)
  else:
    print(0)
  
# verificando se o grafo é conexo
for grafo in grafos:
  links = grafo['links']
  vertices = grafo['vertices']
  visitados = []

  # print("Criando matriz ",int(vertices),"x", int(vertices))
  if int(vertices) > 10:
    imprime_saida(False)
    continue

  #preenche a matriz visitados em branco
  for i in range(int(vertices)):
    visitados.append([])

    for j in range(int(vertices)):
      visitados[i].append(0)

  #MATRIZ DE ADJACÊNCIAS
  #verificar se é possível partir do primeiro nó e ir até todos
  for vertice in range(1, int(vertices)+1):

    for link in links:
      link = link.split()

      inicio = int(link[0])
      fim = int(link[1])
      direcao = int(link[2])

      if inicio == vertice:

        # se for bidirecional, os dois sentidos pontuam
        if direcao == 2:
          visitados[vertice-1][fim-1] = 1
          visitados[fim-1][vertice-1] = 1

        # se for unidirecional, apenas um sentido pontua
        elif direcao == 1:
          visitados[fim-1][vertice-1] = 1


  # print(visitados) #[[0, 1, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 0]]

  # verificar se a matriz foi percorrida
  x = verifica_conexao(visitados)

  imprime_saida(x)
