class Edge:
    def __init__(self, v, u, w):
        self.v = v
        self.u = u
        self.w = w

def compara(a, b):
    return a.w - b.w

def componente(i):
    if i == p[i]:
        return i
    return componente(p[i])

def kruskal(c):
    ans = 0
    for i in range(c):
        v = componente(g[i].v)
        u = componente(g[i].u)
        if v != u:
            p[v] = p[u]
            ans += g[i].w
    return ans

r, c = map(int, input().split())
g = []
p = [i for i in range(r + 1)]

for i in range(c):
    v, u, w = map(int, input().split())
    g.append(Edge(v, u, w))

g.sort(key = lambda x: x.w)
print(kruskal(c))
