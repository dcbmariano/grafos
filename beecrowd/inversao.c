#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define false 0
#define true 1

typedef struct __fila__no{
    // nó da fila
    int data;
    struct __fila__no *prox;
} fila_no;

typedef struct __fila__type{
    // tipo / fila
    fila_no *inicio;
    fila_no *fim;
} fila_t;

int a,b;

int d[100010];

// variaveis
void busca_em_profundidade(int);
void pop(fila_t *);
int front(fila_t *);
_Bool vazio(fila_t *);
void push(fila_t *, int);
void cria_fila(fila_t *);

int main(int argc, char **argv){
    // principal
    int t;
    scanf("%d", &t);

    while(t--){
        memset(d, -1, sizeof(d));
        scanf("%d %d", &a, &b);
        busca_em_profundidade(a);
        printf("%d\n", d[b]);
    }
    return 0;
}

void busca_em_profundidade(int u){
    // realiza uma busca em profundidade
    fila_t fila; 
    cria_fila(&fila); // cria a fila
    push(&fila, u);

    d[u] = 0;

    while (!vazio(&fila)){
        // enquanto a fila nao estiver vazia
        int v = front(&fila);

        if (d[b] != -1)
            break;
        pop(&fila); // remove elemento

        int invert = 0, uu = v;
        while (uu){
            invert *= 10;
            invert += uu % 10;
            uu /= 10;
        }
        if (d[invert] == -1)
            d[invert] = d[v] + 1, push(&fila, invert);
        if (d[v + 1] == -1)
            d[v + 1] = d[v] + 1, push(&fila, v + 1);
    }
}

void cria_fila(fila_t *__fila){
    // cria a fila
    __fila->inicio = NULL; // posicao inicial
    __fila->fim = NULL;    // posicao final
}

void push(fila_t *__fila, int __data){
    // adiciona elemento na fila
    fila_no *tmp;  
    tmp = (fila_no *) malloc(sizeof(fila_no));

    if (__fila->inicio)
        __fila->fim->prox = tmp;
    else
        __fila->inicio = tmp;

    tmp->prox = NULL;
    __fila->fim = tmp;
    tmp->data = __data;

}

void pop(fila_t *__fila){
    // remove elemento da fila
    fila_no *tmp;

    if (__fila->inicio){
        // se a fila estiver no inicio
        if (__fila->inicio->prox){
            tmp = __fila->inicio;
            __fila->inicio = __fila->inicio->prox;
            free(tmp);              
        }
        else{
            tmp = __fila->inicio;
            __fila->inicio = __fila->fim = NULL;
            free(tmp);   
        }
    }
    else
        return;
}

_Bool vazio(fila_t *__fila){
    return __fila->inicio == NULL;
}

int front(fila_t *__fila){
    return __fila->inicio->data;
}