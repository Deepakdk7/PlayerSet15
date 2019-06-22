ax=list(map(int,input().split()))
a=list(map(int,input().split()))
k=ax[1]
c=[]
d=[]
for i in range(0,k):
    c.append(a[i])
c.sort()
for i in range(k,ax[0]):
    d.append(a[i])
d=sorted(d)[::-1]
print(*c+d)
