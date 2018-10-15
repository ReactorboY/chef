t=int(input())
occur=[]
for i in range(t):
    num=int(input())
    count=0
    while(num!=0):
        if(num%10==4):
            count+=1
        num=num//10
    occur.append(count)

for i in range(len(occur)):
    print(occur[i])
