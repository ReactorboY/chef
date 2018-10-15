t=int(input())
a=[]
for i in range(t):
    n=int(input())
    s=list(str(n))
    b=int(s[0])+int(s[len(s)-1])
    a.append(b)

for i in range(t):
    print(a[i])
