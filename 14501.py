import sys
input=sys.stdin.readline

n=int(input())
T=[0]*(n+1)
P=[0]*(n+1)

for i in range(1,n+1):
    a,b=map(int,input().split())
    T[i]=a
    P[i]=b

dp = [0]*(n+1) #dp[i]: i날까지의 수익

for i in range(1,n+1):
    dp[i+1]=max(dp[i+1],dp[i]) #다음날에 현재까지의 수익 전달받음

    if i+T[i]<=n+1:


    #수익 (dp[i]+P[i])
    #다음 상담 가능날 (i+T[i])
    
print(dp[n+1])
