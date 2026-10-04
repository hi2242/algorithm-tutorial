# 문제 정보
# n명의 권투선수 (1번 ~ n번)
# 1대1 경기, 실력이 좋은 선수가 항상 이김
# 결과 분실로 정확한 순위를 매길 수 없음
# 순위를 매길 수 있는 선수의 수 구하기

# 입력 정보
# n -> 선수의 수
# results -> 경기 결과를 담은 2차원 배열 ([A, B] -> A가 B를 이긴다)

# 반환 정보
# answer -> 순위를 매길 수 있는 선수의 수

def solution(n, results):
    answer = 0
    result_grid = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for a, b in results:
        # 이기면 2, 지면 1, 모르면 0
        result_grid[a][b] = 2
        result_grid[b][a] = 1
    floyd(n, result_grid)

    for r in range(1, n + 1):
        count = 0
        for c in range(1, n + 1):
            if result_grid[r][c] != 0:
                count += 1
        if count == n - 1:
            answer += 1
    return answer

def floyd(n, grid):
    for stop in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                if grid[start][stop] == 2 and grid[stop][end] == 2:
                    grid[start][end] = 2
                    grid[end][start] = 1
                
def print_grid(grid):
    for row in grid:
        print(*row)
    print()