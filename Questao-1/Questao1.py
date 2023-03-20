MAXSIZE = 26
visitados = [0] * MAXSIZE
adj = [[0] * MAXSIZE for _ in range(MAXSIZE)]
vertices = [''] * MAXSIZE
tam = 0
m, n = 0, 0

def dfs(u):
    global tam
    visitados[u] = 1
    vertices[tam] = chr(u + ord('a'))
    tam += 1
    for i in range(m):
        if adj[u][i]:
            if not visitados[i]:
                dfs(i)

def compara(a, b):
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1

casos = int(input())

for caso in range(1, casos + 1):
    m, n = map(int, input().split())
    
    for i in range(n):
        a, b = input().split()
        a, b = ord(a) - ord('a'), ord(b) - ord('a')
        adj[a][b] = 1
        adj[b][a] = 1
    
    print(f'Case #{caso}:')
    ans = 0
    for i in range(m):
        if not visitados[i]:
            ans += 1
            dfs(i)
            vertices.sort(key=lambda x: ord(x) if x != '' else 120)
            print((','.join(vertices[:tam])) + ',')
        tam = 0
    
    print(f'{ans} connected components\n')
    visitados = [0] * MAXSIZE
    adj = [[0] * MAXSIZE for _ in range(MAXSIZE)]
    vertices = [''] * MAXSIZE