N=int(input())
lst=list(map(int,input().split()))
cnt=0
result=0

def milk (result):
    for i in range(2):
        if i==2:
            result=0
        else: 
            result=i+1
    return result

for i in range(N):
    if lst[0]!=0:
        break
    else:
        
        if milk(result):
            cnt+=1
        
        
print(cnt)
    