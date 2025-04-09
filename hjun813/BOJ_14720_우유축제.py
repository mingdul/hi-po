# 배열에서 0,1,2 순서대로 횟수를 올려주면 된다. 
# 최대 개수가 궁금하기 때문에
# 다음 순서를 만나는 대로 마셔야 최대개수가 된다.

import sys
input = sys.stdin.readline

N = int(input()) # 가게 수
store = list(map(int, input().split())) # 가게 정보

needToDrink = 0 # 이번에 마실거
drink = 0 # 마신 횟수

for milk in store: # 가게 배열 순서 대로 확인
    if milk == needToDrink: # 이번에 마실거랑 같으면 
        drink += 1 # 마신 횟수
        needToDrink += 1 # 다음에 마실거 넘버링
        needToDrink = needToDrink % 3 # 0,1,2 에서만 놀아야 하니까  
        

print(drink) 
