a,b,c = input().split()
a=int(a)
b=int(b)
c=int(c)

for i in a,b,c:
    if i % 2 == 1:
        print("odd")
    if i % 2 == 0:
        print("even")
