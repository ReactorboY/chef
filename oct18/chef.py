t=int(input())
for i in range(t):
    p1,p2,k=map(int,input().split())
    tl=p1+p2
    rem=tl%k
    tl=tl-rem
    turn="A"
    if(tl%k==0):
        tl //= k
        if(tl%2==0):
            turn="CHEF"
        else:
            turn="COOK"
    else:
        tl-=1
        tl //= k
        if(tl%2==0):
            turn="CHEF"
        else:
            turn="COOK"
    print(turn)
