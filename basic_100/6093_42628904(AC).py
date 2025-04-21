n = int(input())
a = map(int, input().split())
a = list(a)

for i in range(n-1,-1,-1):
    print(a[i], end=' ')
