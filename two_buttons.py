from queue import Queue

s = input().strip().split(' ')
n = int(s[0])
m = int(s[1])

g = [[] for i in range(20_000 + 1)]

for i in range(1, 10_001):
    if i < m:
        g[i].append(i * 2)

for i in range(2, 20_001):
    g[i].append(i - 1)

out = [0] * (20_000 + 1)
q = Queue()
q.put((n, 0))

while not q.empty():
    curr = q.get()
    for i in g[curr[0]]:
        if i == m:
            print(curr[1] + 1)
            exit(0)
        q.put((i, curr[1] + 1))
        out[curr[0]] = 1
