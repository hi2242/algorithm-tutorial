# 문제 정보
# 노드에 늑대와 양이 한 마리씩 있음
# 루트에서 출발해서 노드를 돌며 양을 모음
# 노드 방문 시 양과 늑대가 따라옴
# 늑대는 늑대의 수 >= 양의 수면 바로 모든 양을 잡아먹음
# 중간에 양이 늑대에게 잡아 먹히지 않도록 최대한 많은 양을 모아 다시 루트로 돌아오기

# 입력 정보
# info -> 각 노드의 양 또는 늑대 정보가 담긴 배열 (양: 0, 늑: 1)
# edges -> 각 노드들의 연결 관계를 담은 2차원 배열

# 반환 정보
# answer -> 각 노드 방문 후 모을 수 있는 양의 최대 마리 수

# 함수 정보
# init -> 트리를 초기화하는 함수

# BFS + 비트마스킹 (다음 노드 / 양의 수 / 늑대의 수 / 방문 비트마스킹 정보)

from collections import deque
        
def solution(info, edges):
    answer = 0
    dq = deque()
    dq.append((0, 1, 0, 1 << len(info) | 1 << 0))
    tree = {i: [] for i in range(len(info))}
    
    def init():
        for edge in edges:
            parent, child = edge
            tree[parent].append(child)
    init()
    
    while dq:
        node_num, sheep_count, dog_count, mask = dq.popleft()

        answer = max(answer, sheep_count)
        
        for next_node_num in tree[node_num]:
            # 다음 노드가 양인 경우
            if info[next_node_num] == 0:
                # 방문하지 않았다면 0번 노드 다시 집어 넣기
                if not (mask & 1 << next_node_num):
                    dq.append((0, sheep_count + 1, dog_count, mask | 1 << next_node_num))
                else:
                    # 방문했다면 카운팅하지 않고 다음 노드 탐색
                    dq.append((next_node_num, sheep_count, dog_count, mask))
            else:
                # 방문하지 않았다면 카운팅 후 잡아먹히지 않는 경우 탐색
                if not (mask & 1 << next_node_num):
                    if sheep_count > dog_count + 1:
                        dq.append((0, sheep_count, dog_count + 1, mask | 1 << next_node_num))
                else:
                    # 방문했다면 카운팅하지 않고 다음 노드 탐색
                    dq.append((next_node_num, sheep_count, dog_count, mask))
            
    return answer