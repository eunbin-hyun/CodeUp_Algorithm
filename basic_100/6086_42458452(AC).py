n = int(input())
s = 0
c = 0

while True:
    c += 1
    s += c
    if s >= n:
        break
    
print(s)
