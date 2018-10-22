from queue import Queue

s = input().strip().split(' ')
n = int(s[0])
m = int(s[1])

if m <= n:
    print(n - m)
    exit(0)

g = [[] for i in range(2 * m - 1)]

for i in range(1, m):
    if i < m:
        g[i].append(i * 2)

for i in range(2, 2 * m - 1):
    g[i].append(i - 1)

out = [0] * (2 * m - 1)
q = Queue()
q.put((n, 0))
out[n] = 1

while not q.empty():
    curr = q.get()
    for i in g[curr[0]]:
        if not out[i]:
            if i == m:
                print(curr[1] + 1)
                exit(0)
            q.put((i, curr[1] + 1))
            out[i] = 1
