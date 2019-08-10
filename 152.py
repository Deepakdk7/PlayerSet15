a=list(input())
n=0
if len(a)>1:
    v=['a','e','i','o','u']
    c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    for i in range(len(a)-1):
        if a[i] in v and a[i+1] in c:
            n=n+1
        if a[i] in c and a[i+1] in v:
            n=n+1
    if (a[-1] in c and a[-2] in v) or (a[-1] in v and a[-2] in c):
        n=n+1
    print(n)
else:
    print(n)
