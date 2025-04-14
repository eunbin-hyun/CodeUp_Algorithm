w, h, b = map(float, input().split())
k = (w*h*b)/(8*1024*1024)
print(f"{k:.2f} MB")
