"""1932 - Bolsa de Valores
Author: Diego Mariano (@dcbmariano)

=== como testar localmente ===
Crie um arquivo chamado "entrada.txt" e coloque a entrada de exemplo dada no beecrowd. Em seguida, execute no terminal com:
python 1932.py < entrada.txt

=== Descrição do exercício === 
Um investidor principiante deseja aprender a investir na p de valores. Como ele não tem experiência, selecionou uma única empresa, e acompanhou os valores diários das ações dessa empresa, durante N n. Ficou curioso quanto teria ganhado se tivesse investido nesse período em que acompanhou os valores. Na verdade, o investidor é milionário e tem muito dinheiro, suficiente para comprar qualquer quantidade de ações da empresa. Entretanto, como é um investidor cuidadoso, decidiu que nunca teria mais do que uma ação da empresa.

Como sempre há intermediários, a corretora de valores cobra uma c fixa de C reais a cada compra de uma ação da empresa.

Você deve calcular qual o lucro máximo que o investidor poderia ter auferido, investindo durante alguns dos N n, podendo inclusive decidir não investir.

Entrada
A primeira linha contém dois inteiros, N e C (1 ≤ N ≤ 2 × 105 e 0 ≤ C ≤ 30).

A segunda linha contém as N cotações P1, P2, . . . , PN , dos n 1, 2, . . . , N, respectivamente. Cada cotação Pi satisfaz as desigualdades 1 ≤ Pi ≤ 1000.

Saída
Seu programa deve produzir uma única linha com um inteiro representando o lucro máximo do investidor, em reais.
"""
# n => dias
# c => custo da transação
# p = cotações
n, c = map(int,input().split()) # A primeira linha contém dois inteiros, N e C
p = input().split() # segunda linha contém as N cotações P1, P2, . . . , PN 
p = [int(i) for i in p] # converte em int

lucro_maximo = 0  # lucro máximo começa em 0

def lucro_eh_positivo(valor_atual, valor_compra, c):
    """ verifica se o lucro é positivo considerando a taxa c"""
    if valor_atual - valor_compra - c > 0:
        return True
    else:
        return False
    
# para cada dia
for i in range(n):
    if i == 0: # primeiro dia 
        valor_atual = p[0]
        valor_compra = p[0]
        continue 
    
    cotacao_dia = p[i] # recebe a cotação do dia "i"

    if ((valor_atual > cotacao_dia and (valor_atual - cotacao_dia >= c)) or cotacao_dia < valor_compra):
        
        # atualizando o lucro maximo 
        if lucro_eh_positivo(valor_atual, valor_compra, c):
            lucro_maximo += valor_atual - valor_compra - c
        valor_atual = cotacao_dia
        valor_compra = cotacao_dia

    # atualiza valor_atual
    if cotacao_dia > valor_atual:
        valor_atual = cotacao_dia

# se o valor atual menos o valor de compra menos o custo de transação é positivo
if lucro_eh_positivo(valor_atual, valor_compra, c):
    lucro_maximo += valor_atual - valor_compra - c 

print(lucro_maximo)
