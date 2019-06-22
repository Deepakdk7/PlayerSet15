ax=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(0,ax):
    for j in range(i+1,ax):
        if a[j]%a[i]==0:
            c.append(a[j])
c=list(dict.fromkeys(c))
print(*c)
