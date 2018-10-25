s = input().strip()
n = len(s)

m = [[1_000_000_000] * n for i in range(n)]
for i in range(n):
    m[i][i] = 1

for k in range(1, n):
    for i in range(n - k):
        for j in range(k):
            if s[i] == s[i + k]:
                m[i][i + k] = min(m[i][i + k], m[i][i + j] + m[i + 1 + j][i + k] - 1)
            else:
                m[i][i + k] = min(m[i][i + k], m[i][i + j] + m[i + 1 + j][i + k])

print(m[0][n - 1])
