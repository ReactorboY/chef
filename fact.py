t=int(input())
a=[]
sum=1
while (t > 0):
    n=int(input())
    while(n>0):
        sum = sum * n
        n-=1
    a.append(sum)
    sum=1
    t-=1

for i in range(len(a)):
    print(a[i])
