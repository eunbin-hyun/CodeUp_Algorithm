d = []
for _ in range(19):
    row = list(map(int, input().split()))
    d.append(row)

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for j in range(19):
        if d[x][j] == 0:
            d[x][j] = 1
        else:
            d[x][j] = 0
            
    for k in range(19):
        if d[k][y] == 0:
            d[k][y] = 1
        else:
            d[k][y] = 0
            
for i in range(19):
    for j in range(19):
        print(d[i][j], end= ' ')
    print()
