ax=list(map(int,input().split()))
a=(ax[0]*ax[1])
c=[]
a=list(bin(a))
a.remove('0')
a.remove('b')
for i in range(0,len(a)):
    if a[i]=='1':
        c.append(i)
if len(c)>=2:
    print(c[1]+1)
else:
    print('0')
