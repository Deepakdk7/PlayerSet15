ax=list(map(int,input().split()))
c=0
a=list(bin(ax[0]*ax[1]))
for i in a:
    if i=='1':
        c=c+1
print(c)
