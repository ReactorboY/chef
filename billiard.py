round = int(input())
a=[]
b=[]
leadA=[]
leadB=[]
for i in range(0,round):
    s,t = map(int,input().split())
    a.append(s)
    b.append(t)

for i in range(0,len(a)):
    if (a[i] > b[i]):
        leadA.append(a[i]-b[i])
    else:
        leadB.append(b[i]-a[i])

if(max(leadA) > max(leadB)):
    print(1,max(leadA))
else:
    print(2,max(leadB))
