# 비트마스킹 + 동적 계획법(DP)으로 문제를 풀어야 한다.
'''
비트 마스킹
0001 (2진수) → 0번 도시만 방문
1011 (2진수) → 0, 1, 3번 도시 방문
1111 (2진수) → 모든 도시 방문

새로운 도시 j 방문 확인
if visited & (1 << j):


'''
import sys

INF = float('inf')

# 입력 받기
n = int(sys.stdin.readline().strip())  # 도시 개수
w = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 비용 행렬

# DP 테이블 (-1로 초기화)
dp = [[-1] * n for _ in range(1 << n)]

# TSP 함수 정의
def tsp(visited, current):
    # 모든 도시를 방문한 경우
    if visited == (1 << n) - 1:
        return w[current][0] if w[current][0] > 0 else INF  # 시작점으로 돌아가는 비용

    # 이미 계산한 값이면 반환
    if dp[visited][current] != -1:
        return dp[visited][current]

    # 최소 비용 초기화
    min_cost = INF

    # 방문하지 않은 모든 도시 탐색
    for next_city in range(n):
        if not (visited & (1 << next_city)) and w[current][next_city] > 0:
            cost = tsp(visited | (1 << next_city), next_city) + w[current][next_city]
            min_cost = min(min_cost, cost)

    # 결과 저장
    dp[visited][current] = min_cost
    return min_cost

# 시작 도시를 0으로 가정하고 TSP 실행
print(tsp(1, 0))
