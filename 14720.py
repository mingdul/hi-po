import sys
input=sys.stdin.readline

N=int(input()) 
M=list(map(int, input().split())) 

drink=0   
cnt=0     

for i in M:
    if i==drink:
        drink=(drink+1)%3
        cnt+=1

print(cnt)