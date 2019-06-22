ax=input().split()
k=int(ax[1])
c=['*']
for i in ax[0]:
    c.append(i)
for i in range(1,len(ax[0])+1):
    if i%k==0:
        print(*c[i],end=' ')
