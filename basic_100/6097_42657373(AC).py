h, w = map(int, input().split())
n = int(input())
d = [[0 for _ in range(w)] for _ in range(h)]

for _ in range(n):
    i, d_dir, x, y = map(int, input().split())
    x -= 1 
    y -= 1 
    
    if d_dir == 0:
        for l in range(i):
            d[x][y+l] = 1
    else:
        for l in range(i):
            d[x+l][y] = 1
            
for i in range(h):
    for j in range(w):
        print(d[i][j], end=' ')
    print()
