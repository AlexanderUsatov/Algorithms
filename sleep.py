s = input().strip().split(' ')
n = int(s[0])
k = int(s[1])
s = input().strip().split(' ')
teo = [0] * n
for i in range(n):
    teo[i] = int(s[i])

s = input().strip().split(' ')
sleep = [0] * n
for i in range(n):
    sleep[i] = int(s[i])

plus = 0
for i in range(k):
    plus += teo[i] * (1 - sleep[i])

max_ = plus

for ptr in range(k, n):
    plus += teo[ptr] * (1 - sleep[ptr]) - teo[ptr - k] * (1 - sleep[ptr - k])
    if plus > max_:
        max_ = plus
        
sum_ = 0
for i in range(n):
    sum_ += teo[i] * sleep[i]
    
print(sum_ + max_)
