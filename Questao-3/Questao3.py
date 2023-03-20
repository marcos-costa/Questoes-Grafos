def dfs(a, grafo, visitados):
    visitados[a] = 1
    for j in range(E):
        if grafo[a][j]:
            if not visitados[j]:
                dfs(j, grafo, visitados)

E, L = [int(x) for x in input().split(' ')]
n = 1
while E != 0:

    grafo = [([0]*E).copy() for x in range(E)]
    
    while L:
        X, Y = [int(x) for x in input().split(' ')]
        grafo[X-1][Y-1] = 1
        L -= 1
    
    visitados = [0] * E
    dfs(0, grafo, visitados)
    print("Teste", n)
    print("normal\n" if sum(visitados) == E else "falha\n")
    n += 1
    E, L = [int(x) for x in input().split(' ')]