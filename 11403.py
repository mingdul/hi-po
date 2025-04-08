import sys
input=sys.stdin.readline

n=int(input())
G=[list(map(int,input().split())) for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if i==j:
#             G[i][j]=0
#             break

for k in range(n):          # 중간
    for i in range(n):      # 출발
        for j in range(n):  # 도착
            

            
            # G[i][j] = min(G[i][j], G[i][k] + G[k][j])

            # G[i][j] 출발-도착
            # G[i][k] 출발-중간
            # G[k][j] 중간-도착

            # G[i][k]=G[k][j] ??
            # G[i][j]
