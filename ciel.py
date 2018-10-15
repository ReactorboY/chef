t=int(input())
a=[1,2,4,8,16,32,64,128,256,512,1024,2048]
p=[]
for i in range(t):
    n=int(input("enter the number "))
    for i in range(len(a)):
        if(n==a[i]):
            p.append(1)
        

for i in range(len(p)):
    print(p[i])
