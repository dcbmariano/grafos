""" Isósceles | 2243
Author: Diego Mariano (@dcbmariano)

=== como testar localmente ===
Crie um arquivo chamado "entrada.txt" e coloque a entrada de exemplo dada no beecrowd. Em seguida, execute no terminal com:
python 2243.py < entrada.txt

=== Descrição do exercício === 
Os irmãos Sérgio e Luiz estavam brincando com cubinhos de madeira e queriam construir um muro, que acabou ficando incompleto, com as colunas tendo diferentes alturas, como nessa figura.

Eles decidiram agora que a brincadeira seria retirar cubinhos, sempre de cima para baixo nas colunas, de maneira que no final restasse apenas um triângulo isósceles de cubinhos. Eles podem apenas retirar cubinhos do muro, sem recolocar em outra coluna, e os triângulos têm que ser completos. A figura abaixo ilustra os cinco primeiros triângulos isósceles de cubinhos, do tipo que eles querem, com alturas 1, 2, 3, 4 e 5 respectivamente.

Dada a sequência de alturas das colunas do muro, seu programa deve ajudar Sérgio e Luiz a descobrir qual é a altura máxima que o triângulo poderia ter ao final. No muro da primeira figura, com 30 colunas de cubinhos, o triângulo mais alto possível teria altura igual a sete.

Entrada
A primeira linha da entrada contém um inteiro N, 1 ≤  N ≤  50000, representando o número de colunas do muro. A segunda linha contém N inteiros Ai, 1 ≤  Ai ≤  N, para 1 ≤  i ≤  N, indicando as alturas de cada coluna.

Saída
Seu programa deve produzir uma única linha com um inteiro H, representando a altura máxima que um triângulo poderia ter ao final.
"""

n = int(input()) # número de colunas do muro N, 1 ≤  N ≤ 50000
colunas = input().split() # pega a altura das colunas
colunas = [int(i) for i in colunas] # converte em int

# vamos dividir o muro ao meio e separar em dois lados: l e r (esquerda e direita)
l = [0]*n  # vamos iniciar a altura com tamanho 0
r = [0]*n  # vamos iniciar a altura com tamanho 0

# para q seja um triangulo, a primeira e última colunas devem ter tamanho 1
l[0] = 1
r[n-1] = 1

# precisamos comparar o lado direito com o lado esquerdo para encontrar a altura máxima 
# lado esquerdo
for i in range(n):
    if i == 0:  # a pemeira nao pode ser maior
        continue 
    
    atual = colunas[i]
    anterior = l[i-1]+1

    l[i] = min(atual, anterior)

# lado direito 
for i in range(n, 0, -1): # lê de tras pra frente
    if i == n or i == n-1: # a ultima ou penultima nao pode ser maior
        continue

    atual = colunas[i]
    posterior = r[i+1]+1

    r[i] = min(atual, posterior)

# obtendo o maior valor de coluna
maior = 0
for i in range(n):
    aux_i = min(l[i], r[i])
    if aux_i > maior:
        maior = aux_i

# === imprime a saída da tela ===
print(maior)