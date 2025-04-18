a,r,n = map(int, input().split())
k=0
s=0

while True:
    k = a*(r**s)
    s += 1
    if s == n:
        print(k)
        break
