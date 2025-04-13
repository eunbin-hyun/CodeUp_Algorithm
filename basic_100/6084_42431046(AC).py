h, b, c, s = map(int, input().split())
k = (h*b*c*s)/8/1024/1024
print(round(k, 1), "MB")
