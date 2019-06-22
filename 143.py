ax=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=dict(zip(b,a))
d=sorted(b)
for i in d:
    print(c.get(i),end=' ')
