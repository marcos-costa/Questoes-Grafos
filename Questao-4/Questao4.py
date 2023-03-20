def dfs(a, grafo, visitados):
    visitados[a] = 1
    for j in range(N):
        if grafo[a][j]:
            if visitados[j]:
                return True
            if dfs(j, grafo, visitados):
                return True
    visitados[a] = 0
    return False

T = int(input())

while T:
    circulo = 0

    N, M = [int(x) for x in input().split(' ')]
    grafo = [([0]*N).copy() for x in range(N)]
    
    while M:
        A, B = [int(x) for x in input().split(' ')]
        grafo[A-1][B-1] = 1
        M -= 1
    
    visitados = [0] * N
    for i in range(N):
        if dfs(i, grafo, visitados):
            circulo = 1
    print("SIM" if circulo else "NAO")
    T -= 1