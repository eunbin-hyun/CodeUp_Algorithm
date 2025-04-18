a,d,n = map(int, input().split())
k=0
s=0

while True:
    k = a + s*d
    s += 1
    if s == n:
        print(k)
        break
