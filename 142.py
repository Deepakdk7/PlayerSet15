ax=list(map(int,input().split()))
k=ax[1]
a=[]
c=1
for i in range(0,ax[0]):
    a.append(input())
for i in range(0,ax[0]):
    for j in range(i+1,ax[0]):
        if a[i]==a[j]:
            c=c+1
    if c==k:
        print('yes')
        break
else:
    print('no')
