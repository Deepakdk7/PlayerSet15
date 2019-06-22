ax=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(0,ax-1):
        if a[i+1]%a[i]==0:
            c.append(a[i+1])
print(*c)
