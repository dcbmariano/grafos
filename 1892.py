"""
beecrowd | 1892
Calouro Vence Veterano?
Author: Diego Mariano (@dcbmariano)

=== como testar localmente ===
Crie um arquivo chamado "entrada.txt" e coloque a entrada de exemplo dada no beecrowd. Em seguida, execute no terminal com:
python 1892.py < entrada.txt

=== Descrição do exercício === 
Professor Denis está curioso para saber se a classificação final de seus N alunos de programação competitiva segue a ordem de matrícula na universidade. Ele pediu a sua ajuda para, dada a classificação final, contar quantos pares (i, j) existem tais que i < j e m[i] > m[j], onde 1 ≤ i,j ≤ N e m[i] significa a matrícula do aluno que ficou em i-ésimo lugar.

Entrada
A entrada contém vários casos de teste.

A primeira linha de um caso de teste contém um único inteiro N, que representa o número de alunos, onde 1 ≤ N ≤ 105.

As próximas N linhas são a classificação final dos alunos. Cada linha contém uma cadeia de exatamente 10 caracteres.

Saída
Para cada caso de teste, imprima uma única linha com o número pedido na especificação.
"""

import time
ini = time.time()

# DIVISÃO E CONQUISTA : MERGE AND COUNT

def merge(esquerda, direita):
    """ mescla as listas """
    resultado = []
    contagem = 0
    i = 0 
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i+=1
        else:
            contagem+=len(esquerda)-i # INVERSAO DETECTADA
            resultado.append(direita[j])
            j+=1
            
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    # retorna a lista ordenada e a contagem de inversões
    return resultado, contagem


def merge_and_count(lista):
    """ algoritmo de divisao e conquista que conta as inversoes """
    if len(lista) <= 1:
        return lista, 0 # caso base

    meio = len(lista) // 2 # determina a metade

    # CHAMADAS RECURSIVAS para esquerda e direita
    esquerda_metade, esquerda_contagem = merge_and_count(lista[:meio]) # chamada recursiva para esquerda
    direita_metade, direita_contagem = merge_and_count(lista[meio:]) # chamada recursiva para direita

    # MESCLA AS LISTAS
    lista_mesclada, split_contagem = merge(esquerda_metade, direita_metade) # mescla
    
    # CONTAGEM DE INVERSOES
    total_contagem = esquerda_contagem + direita_contagem + split_contagem
    
    return lista_mesclada, total_contagem

x = [10,1,4,5,8,2,6,9,3,7]
cont = 0
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i] > x[j]:
            cont+=1
            print(cont, x[j], '>', x[i])

print(cont)


while True:
    try:
        n = int(input())
        m = [int(input().replace('/','')) for i in range(n)]

        cont = 0
        # ESTRATÉGIA 1 = FORÇA BRUTA
        # tam = len(m)
        # for i in range(0, tam-1):
        #     for j in range(i, tam):
        #         if m[i] > m[j]:
        #             cont+=1

        # ESTRATEGIA 2 = DIVISÃO E CONQUISTA
        ordenado, cont = merge_and_count(m)

        print(cont)
    except:
        break


fim = time.time()

#print(fim-ini,'seg')