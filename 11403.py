import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

# 잘 모르겠지만 일단 플로이드 워셜 돌렸음
for k in range(N):
    for i in range(N):
        for j in range(N):
            # 길이 연결되어 있으면 연결되어있다고 해라
            if matrix[i][k] == 1 and matrix[k][j] == 1: 
                matrix[i][j] = 1

for i in range(N):
    print(*matrix[i])