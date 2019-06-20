ax=int(input())
a=[]
for i in range(0,ax):
    a.append(input())
for i in range(0,ax-1):
    if a[i]==a[i+1]:
        print('yes')
        break
else:
    print('no')
