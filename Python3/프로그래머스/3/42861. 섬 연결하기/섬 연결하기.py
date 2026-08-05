# 문제 정보
# 주어진 다리 건설 비용을 기준으로 최대한 싸게 모든 섬을 연결하는 비용 찾기

# 입력 정보
# n -> 섬의 개수
# costs -> 다리 건설 비용 (2차원 배열) [A섬, B섬, A-B 다리 건설 비용]

# 반환 정보
# answer -> 섬 연결 후 최소 비용

# 풀이 방법 (크루스칼 알고리즘)
# 1. PQ에 다리 건설 정보를 넣는다.
# 2. PQ에서 싼 것부터 꺼내서 섬을 연결
# 3. set에 방문한 섬 넣고 길이가 n이 되면 모두 연결된지 체크
# 4. map에 넣었던 섬 연결 정보를 타고 visited를 도입하여 set의 길이가 n이 된다면 모두 연결 판정
# 5. 모든 섬이 연결되었을 때가 최소값

import heapq
from collections import deque

def solution(n, costs):
    answer = 0
    pq = []
    parent = [i for i in range(n)]
    
    # pq에 연결 정보 다 넣기
    for bridge in costs:
        heapq.heappush(pq, [bridge[2], bridge[0], bridge[1]])
    
    b_count = 0
    while pq:
        # 연결 정보를 하나씩 꺼내서 딕셔너리와 세트에 저장
        cost, f_island, s_island = heapq.heappop(pq)
        # 두 섬이 하나로 연결되어 있지 않다면 사이클이 아니므로 연결
        if find(parent, f_island) != find(parent, s_island):
            union(parent, f_island, s_island)
            answer += cost
            b_count += 1
        # 만약 세트의 길이가 n(모든 섬을 방문)이고 모든 섬이 연결된지 확인
            if b_count == n - 1:
                break
    return answer

# Union-Find를 통해 사이클 판별
def find(parent, x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    
    if root_a != root_b:
        parent[root_b] = root_a
    

