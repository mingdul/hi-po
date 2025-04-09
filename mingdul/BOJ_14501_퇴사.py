N=int(input())

# T,P=list(map(int,input().split) for _ in range(N))
arr=[]
for _ in range(N):
    T,P=map(int,input().split())
    arr.append((T,P))

W=[]
Wei=[[0]*N]

for i in range(N):
    d=arr[i][0]
    w=arr[i][1]
    if i + d > N:
        Wei[i]=max(w[i],w[i-1])
        W+=Wei[i]
        # dp[i]=max(dp[i-1],dp[i])
    else:
        Wei[i]=max(Wei[i+d],w[i]+Wei[i])
