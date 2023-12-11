def cria_fila():
    # cria uma fila
    fila = {"inicio": None, "fim": None}
    return fila

def push(fila, data):
    # adiciona elemento na fila
    aux = {"data": data, "proximo": None}

    if fila["inicio"] is not None:
        fila["fim"]["proximo"] = aux
    else:
        fila["inicio"] = aux

    fila["fim"] = aux

def pop(fila):
    # retira elemento da fila
    if fila["inicio"] is not None:
        if fila["inicio"]["proximo"] is not None:
            aux = fila["inicio"]
            fila["inicio"] = fila["inicio"]["proximo"]
        else:
            aux = fila["inicio"]
            fila["inicio"] = fila["fim"] = None
        del aux

def ta_vazio(fila):
    # verifica se a fila tá vazia
    return fila["inicio"] is None

def front(fila):
    return fila["inicio"]["data"]

def busca_em_largura(u):
    # realiza uma busca em largura
    global tmp, b
    fila = cria_fila()
    push(fila, u)
    tmp[u] = 0
    while not ta_vazio(fila):
        v = front(fila)
        if tmp[b] != -1:
            break
        pop(fila)
        rev, uu = 0, v
        while uu > 0:
            rev *= 10
            rev += uu % 10
            uu //= 10
        if tmp[rev] == -1:
            tmp[rev] = tmp[v] + 1
            push(fila, rev)
        if tmp[v + 1] == -1:
            tmp[v + 1] = tmp[v] + 1
            push(fila, v + 1)

# começa o código aqui
tmp = [-1] * 10000  # limita a 10000
#print(tmp)
a, b = map(int, "808 909".split())

busca_em_largura(a)

print(tmp[b])