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
            if G[i][k] == 1 and G[k][j] == 1: 
                G[i][j] = 1

for i in range(n):
    print(*G[i])