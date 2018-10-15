t=int(input())
while t > 0:
    s=1
    n=int(input())
    for i in range(1,n+1):
        s=s*i
    print(s)
    t-=1
