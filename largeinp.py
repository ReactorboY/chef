n,k = input().split()
n=int(n)
k=int(k)
count=0
while(n>0):
    t = int(input())
    if (t % k == 0):
        count += 1
    n = n - 1

print(count)
