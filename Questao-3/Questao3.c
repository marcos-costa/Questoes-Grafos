#include <stdio.h>
#include <string.h>

int E, L, X, Y, falha, n = 1;

void dfs(int a, int grafo[E][E], int visitados[E]){
    visitados[a] = 1;
    for (int j = 0; j < E; j++){
        if (grafo[a][j]){
            if (!visitados[j]){
                dfs(j, grafo, visitados);
            }
        }
    }
}

int main(){
    scanf("%d %d", &E, &L);
    
    while(E != 0){
        int grafo[E][E];
        memset(grafo, 0, sizeof(grafo));

        while(L--){
            scanf("%d %d", &X, &Y);
            grafo[X-1][Y-1] = 1;
        }

        int visitados[E];
        memset(visitados, 0, sizeof(visitados));

        dfs(0, grafo, visitados);
        falha = 0;
        for(int i = 0; i < E; i++){
            if (!visitados[i]){
                falha = 1;
                break;
            }
        }
        if (falha) printf("Teste %d\nfalha\n\n", n);
        else printf("Teste %d\nnormal\n\n", n);
        n++;

        scanf("%d %d", &E, &L);
    }
    return 0;
}