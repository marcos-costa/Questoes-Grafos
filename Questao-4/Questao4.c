#include <stdio.h>
#include <string.h>

int N, circulo;

void dfs(int a, int grafo[N][N], int visitados[N]){
    if (circulo) return;

    visitados[a] = 1;
    for (int j = 0; j < N; j++){
        if (grafo[a][j]){
            if (visitados[j]){
                circulo = 1;
            }
            else{
               dfs(j, grafo, visitados); 
            }
        }
    }
    visitados[a] = 0;
}

int main(){
    int T, M, A, B;

    scanf("%d", &T);
    while(T--){
        circulo = 0;
        scanf("%d %d", &N, &M);

        int grafo[N][N];
        memset(grafo, 0, sizeof(grafo));

        while(M--){
            scanf("%d %d", &A, &B);
            grafo[A-1][B-1] = 1;
        }


        int visitados[N];
        memset(visitados, 0, sizeof(visitados));

        for (int i = 0; i < N; i++){
            dfs(i, grafo, visitados);
            if (circulo) break;
        }
        
        if (circulo) printf("SIM\n");
        else printf("NAO\n");

    }
    return 0;
}