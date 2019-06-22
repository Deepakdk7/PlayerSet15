ax=list(map(int,input().split()))
c=d=1
for i in range(1,ax[0]+1):
    c=c*i
for j in range(1,ax[1]+1):
    d=d*j
print(c//d)
