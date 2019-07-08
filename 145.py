ax=int(input())
a=list(map(int,input().split()))
for i in range(0,ax-1):
    if a[i+1]-a[i]==1:
        print('yes')
        break
else:
    print('no')
