import sys
import heapq
N = int(sys.stdin.readline())
lists = []
for i in range(N):
    t, m = map(int, sys.stdin.readline().split())
    e = t + i
    heapq.heappush(lists, [e,i+1,m])
day = 0
cnt = 0
while lists :
    end,start, money = heapq.heappop(lists)
    if day < start :
        if N>= end :
            day = end
            cnt += money

print(cnt)
