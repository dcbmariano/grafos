""" Inversão - 1550
Author: Diego Mariano (@dcbmariano)

=== como testar localmente ===
Crie um arquivo chamado "entrada.txt" e coloque a entrada de exemplo dada no beecrowd. Em seguida, execute no terminal com:
python 1550.py < entrada.txt

=== Descrição do exercício === 
Pedro é um garoto curioso que gostava de eletrônica. Certo dia, o menino estava mexendo no laboratório de sua escola e encontrou uma caixa cheia de pequenos aparelhos eletrônicos feitos por outros alunos em anos anteriores.

Dentro dessa caixa havia um aparelho que possuía apenas um visor e dois botões. Esse visor apresentava um número inteiro. Mexendo nos botões, Pedro descobriu para que servia cada um deles. O primeiro botão adicionava uma unidade ao número no visor. O segundo botão invertia os dígitos do número, por exemplo, 123 invertido resulta em 321 e 150 invertido resulta em 51 (ignora-se os zeros a esquerda).

Inicialmente, o visor apresentava o número A. Após a descoberta da função dos botões, Pedro quer saber como fazer o número do visor mudar de A para um número maior igual a B. O seu trabalho nesse problema é ajudar Pedro a descobrir qual é o número mínimo de apertos de botão para que o número no visor passe a ser igual a B.

Entrada
A entrada é iniciada por um inteiro T, 0 < T ≤ 500, que indica a quantidade de casos de teste a ser processados. Segue-se T linhas cada uma contendo dois inteiros A e B, 0 < A < B < 10000, indicando respectivamente o número inicial no visor e o número que deve ser mostrado no visor depois de apertar os botões.

Saída
Para cada caso de teste, o programa deve imprimir um inteiro indicando o número mínimo de apertos de botão para que o número do visor passe de A para B.
"""
from collections import deque    
import time

inicio = time.time()

"""  Função de inversão:
        (Parte A) mult numero por 10 e soma com resto da divisao por 10
        (Parte B) divide o valor por 10 (faz isso enquanto numero > 0)
        EX: entrada 901 / saida esperada 109
            A) se inverso = 0, inverso * 10 = 0 e numero%10 = 1, então inverso = 1
            B) divisão inteira de 901 por 10 dá 90
            numero = 90
            roda de novo
            A) 1 * 10 + 0 logo inverso = 10
            B) numero = 9
            roda de novo 
            A) 10*10 + 9 = 109 (saida esperada)
            B) numero = 9//10 = 0 (pare)
"""
def inverte(numero):
    inverso = 0 
    while numero > 0:
        inverso = inverso * 10 + numero % 10
        numero //= 10
    return inverso

# pega a primeira linha com quantos números se deseja avaliar
n = int(input()) 


while n > 0:
    apertos_botao = [-1]*99999
    a, b = map(int, input().split())  # a => valor inicial / b => valor final
    
    fila = deque()
    fila.append(a)  # adiciona "a" a fila
    apertos_botao[a] = 0 
    inverso_antigo = 0
    tmp = set()

    # a estratégia é parecida com uma busca em largura, usando uma fila para avaliar os elementos
    while fila:

        valor_atual = fila.popleft()
        # interrompe se já soubermos o valor de apertos para b
        if apertos_botao[b] > 0:
            break
        
        inverso = inverte(valor_atual)

        if apertos_botao[inverso] == -1:
            apertos_botao[inverso] = apertos_botao[valor_atual] + 1
            fila.append(inverso)

            #apertos_botao[inverso_antigo] = -1
            #inverso_antigo = inverso

        if apertos_botao[valor_atual + 1] == -1:
            apertos_botao[valor_atual + 1] = apertos_botao[valor_atual] + 1
            
            fila.append(valor_atual + 1)

            

    print(apertos_botao[b])


    n-=1

fim = time.time()

#print(round(fim-inicio, 3))