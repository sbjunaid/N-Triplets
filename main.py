import math
for _ in range(int(input())):
    N=int(input())
    
    l=[]
    for i in range(2,math.ceil(math.sqrt(N))):
        if N%i==0:
            l=[i,int(N/i),1]   # we need only 3 nos right. So 1 can be one no., 
                               # the N's half can be another one and last one can be that no which is divisible by N other than half.Isnt it simple
    if l:
       print(*l)
    else:
        print(-1)
