m = [[0 for _ in range(10)] for _ in range(10)]

for i in range(10):
    m[i] = list(map(int, input().split()))

a = 1 
b = 1
m[1][1] = 9

while True:
    if m[a][b+1] == 2:
        m[a][b+1] = 9
        break
    elif m[a][b+1] == 1 and m[a+1][b] == 2:
        m[a+1][b] = 9
        break
    
    if m[a][b+1] == 0:
        m[a][b+1] = 9
        b += 1 
    elif m[a][b+1] == 1 and m[a+1][b] == 0:
        m[a+1][b] = 9
        a += 1
    else:
        break
    
for i in range(10):
    for j in range(10):
        print(m[i][j], end= ' ')
    print()
