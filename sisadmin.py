s = input().strip().split(' ')

n = int(s[0])
m = int(s[1])
v = int(s[2]) - 1

if m > (n - 1) * (n - 2) / 2 + 1 or m < n - 1:
    print(-1)
    exit(0)

if v == 0:
    ignore = n - 1
else:
    ignore = 0

for i in range(0, n):
    if i != v:
        print(str(i + 1) + ' ' + str(v + 1))
m -= n - 1

for i in range(0, n):
    if i == v or i == ignore:
        continue
    for j in range(i + 1, n):
        if m == 0:
            exit(0)
        if j == v or j == ignore:
            continue
        print(str(i + 1) + ' ' + str(j + 1))
        m -= 1
