import sys
input = sys.stdin.readline

N, K = map(int, input().split())

Weigths = [0] * (N)
Values = [0] * (N)

for i in range(0, N):
    W, V = map(int, input().split())
    Weigths[i] = W
    Values[i] = V

def knapsack(values, weights, capacity):
    memo = {}

    def helper(index, remaining_capacity):
        # 기저 조건 : 인덱스가 아이템 배열 범위를 벗어나거나 남은 용량이 없는 경우
        if index >= len(values) or remaining_capacity <= 0:
            return 0
        
        # 이전에 계산한 값이 있을 경우
        if (index, remaining_capacity) in memo:
            return memo[(index, remaining_capacity)]
        
        # 현재 아이템을 넣지 않는 경우
        not_take = helper(index + 1, remaining_capacity)

        # 현재 아이템을 넣을 수 있다면 넣는 경우도 고려
        take = 0
        if weights[index] <= remaining_capacity:
            take = values[index] + helper(index + 1, remaining_capacity - weights[index])

        # 최대 가치를 메모하고 반환
        memo[(index, remaining_capacity)] = max(take, not_take)
        return memo[(index, remaining_capacity)]
    
    # helper 함수를 초기 값과 함꼐 호출
    return helper(0, capacity)

max_value = knapsack(Values, Weigths, K)

print(max_value)