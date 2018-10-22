import sys

sys.setrecursionlimit(10_000)

n = int(input())

snm = [-1 for i in range(n)]


def find_set(i):
    if snm[i] < 0:
        return i
    snm[i] = find_set(snm[i])
    return snm[i]


def union_sets(a, b):
    if snm[a] > snm[b]:
        snm[b] += snm[a]
        snm[a] = b
    else:
        snm[a] += snm[b]
        snm[b] = a


rem = []
build = []

count = 0
for i in range(n - 1):
    s = input().strip().split(' ')
    v = int(s[0]) - 1
    w = int(s[1]) - 1
    a = find_set(v)
    b = find_set(w)
    if a == b:
        rem.append((v, w))
        count += 1
    else:
        union_sets(a, b)

print(count)

head = 0
while snm[head] >= 0:
    head += 1
j = head + 1

for i in range(count):
    while snm[j] >= 0:
        j += 1
    print(str(rem[i][0] + 1) + ' ' + str(rem[i][1] + 1) + ' ' + str(head + 1) + ' ' + str(j + 1))
    j += 1
