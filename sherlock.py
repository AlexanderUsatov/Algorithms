s = input().strip().split(' ')
n = int(s[0])
m = int(s[1])
k = int(s[2])

if k == 1:
    print(0)
    exit(0)

snm = [-1] * n


def find_set(i):
    if snm[i] < 0:
        return i
    snm[i] = find_set(snm[i])
    return snm[i]


def union_set(a, b):
    if snm[a] < snm[b]:
        snm[a] += snm[b]
        snm[b] = a
    else:
        snm[b] += snm[a]
        snm[a] = b


count = n
for i in range(m):
    s = input().strip().split(' ')
    v = int(s[0]) - 1
    w = int(s[1]) - 1
    a = find_set(v)
    b = find_set(w)
    if a != b:
        count -= 1
        union_set(a, b)

res = 1
for i in range(n):
    if snm[i] < 0:
        res *= (-1 * snm[i]) % k

if count == 1:
        print(1)
else:
    print(res * pow(n, count - 2, k) % k)
