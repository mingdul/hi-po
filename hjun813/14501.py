# ㅈㅈ
import sys
input = sys.stdin.readline
N = int(input())
plan = []
for _ in range(N):
    T, P = map(int, input().split())
    plan.append((T, P))

print(plan)

# dp를 잘써봅시다

dp = [[0 for _ in range(N+1)] for _ in range(N)]


for i in range(N):
    time, value = plan[i]
    for v in range(time):
        if v+i < N:
            dp[i][v+i] = value
        else:
            dp[i][-1] = -1
for i in range(len(dp)):
    print(dp[i])

print()
for i in range(N):
    for j in range(i):
        if dp[j][i] != 0:
            continue
        else:
            if dp[j][-1] != -1:
                dp[j][i] = dp[i][i]
for i in range(len(dp)):
    print(dp[i])
    
