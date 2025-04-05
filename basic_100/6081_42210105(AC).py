n = input()

for i in range(1,16):
    print(n, '*%X'%i, '=%X'%(int(n, 16)*i), sep='')
