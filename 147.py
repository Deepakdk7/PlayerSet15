ax=input().split()
c=[]
for i in range(0,len(ax)):
    if i>0 and i<len(ax)-1:
        ax[i]=ax[i][::-1]
    c.append(ax[i])
print(*c) 
