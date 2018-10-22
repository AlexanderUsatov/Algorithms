import sys

sys.setrecursionlimit(1_000_000_000)

n = int(input())

points = []

y_for_x = [[] for i in range(1000)]
x_for_y = [[] for i in range(1000)]
for i in range(n):
    s = input().strip().split(' ')
    y_for_x[int(s[0]) - 1].append(int(s[1]) - 1)
    x_for_y[int(s[1]) - 1].append(int(s[0]) - 1)
    points.append([int(s[0]) - 1, int(s[1]) - 1])

count_used = 0

out = [[0] * 1000 for i in range(1000)]


def dfs(x, y):
    out[x][y] = 1
    for yy in y_for_x[x]:
        if not out[x][yy]:
            dfs(x, yy)
    for xx in x_for_y[y]:
        if not out[xx][y]:
            dfs(xx, y)


res = -1

for i in points:
    if not out[i[0]][i[1]]:
        res += 1
        dfs(i[0], i[1])

print(res)
