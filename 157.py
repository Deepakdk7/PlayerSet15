ax=list(map(int,input().split()))
a=(ax[0]*ax[1])
c=1
a=list(bin(a)[::-1])
for i in a:
    if i=='0':
        c=c+1
    else:
        print(c)
        break
