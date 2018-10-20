from queue import PriorityQueue
from math import inf
import sys

sys.setrecursionlimit(1_000_000_000)

s = input().strip().split(' ')
n = int(s[0])
m = int(s[1])
g = [[] for i in range(n)]
way_to = [inf] * n
way_to[0] = 0
out = [0] * n
par = [-1] * n


def way(v):
    if par[v] == -1:
        print(v + 1)
        return
    way(par[v])
    print(v + 1)


for i in range(m):
    s = input().strip().split(' ')
    v = int(s[0]) - 1
    w = int(s[1]) - 1
    if v != w:
        weight = int(s[2])
        g[v].append((w, weight))
        g[w].append((v, weight))

q = PriorityQueue()
q.put((0, 0))
for i in range(n):
    if q.empty():
        break
    now = q.get()
    if out[now[1]] == 1:
        continue
    out[now[1]] = 1
    for j in g[now[1]]:
        if not out[j[0]]:
            if way_to[now[1]] + j[1] < way_to[j[0]]:
                way_to[j[0]] = way_to[now[1]] + j[1]
                par[j[0]] = now[1]
                q.put((way_to[j[0]], j[0]))

if way_to[n - 1] == inf:
    print(-1)
else:
    way(n - 1)
