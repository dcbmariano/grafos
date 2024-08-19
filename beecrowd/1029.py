# -*- coding: utf-8 -*-
'''
Fibonacci, Quantas Chamadas?
beecrowd | 1029
Autor: Diego Mariano
'''


# estratégia 1: contar as ocorrências (funciona, mas não roda no tempo max)

#def fibonacci(x):
#    global num_chamadas, resultados
#    if x == 0 or x == 1:
#      if x == 0:
#          num_chamadas += 1
#          return x  # caso base
#      elif x == 1:
#          num_chamadas += 1
#          resultados += 1
#          return x  # caso base
#    num_chamadas += 1
#    return fibonacci(x-1) + fibonacci(x-2)


# estratégia 2: não calcular o fibonnaci, mas apenas contar a interações

x_max = 39 # valor maximo de x definido na descrição do problema
valores_fibonnaci = [0, 1]
chamadas = [1, 1]

for i in range(x_max):
  # calcula todos os valores de finonacci uma única vez (performance)
  valores_fibonnaci.append(valores_fibonnaci[i] + valores_fibonnaci[i+1])

  # calcula as chamadas (formula: segunda_anterior + anterior + 1)
  chamadas.append(chamadas[i] + chamadas[i+1] + 1)

#print(chamadas)

n = int(input())  # recebe a primeira linha

import time
ini = time.time()

for i in range(n):  # para cada linha remanescente

    x = int(input())  # valor na linha

    #fibonacci(x)  # chama a função fibonacci

    print("fib(", x, ") = ", chamadas[x]-1, " calls = ", valores_fibonnaci[x], sep="")

fim=time.time()
#print(fim-ini,"seg")