n=int(input())
for i in range(n):
    a,b=input().split()
    a=float(a)
    f=0
    if(a>1000):
        f=1
    b=float(b)
    c=a*b
    if(f==1):
        k=c*0.1
        c=c-k
    print("%.6f"%c)
