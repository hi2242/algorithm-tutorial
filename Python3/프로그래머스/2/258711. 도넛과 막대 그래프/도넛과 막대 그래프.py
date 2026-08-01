# [0] 기본 정보
# 그래프 종류 -> 1개 이상의 정점, 단방향 간선
    # 도넛 모양 그래프
    # 막대 모양 그래프
    # 8자 모양 그래프
# 크기가 n인 도넛 모양 그래프 -> n개의 정점 + n개의 간선
# 크기가 n인 막대 모양 그래프 -> n개의 정점 + n - 1개의 간선
# 크기가 n인 8자 모양 그래프 -> (2n + 1)개의 정점 + (2n + 2)개의 간선

# 문제의 순서
# 1. 여러 개의 그래프가 있을 때 허공에 정점을 하나 만든다.
# 2. 생성한 정점을 각 그래프의 임의의 정점 하나로 향하는 간선들 연결
# 3. 각 정점에 서로 다른 번호 매김
# 4. 간선 정보가 주어지면 생성한 정점의 번호와 정점을 생성하기 전 각 그래프의 수를 구함

# 입력 정보
# edges -> 간선 정보를 담은 2차원 정수 배열

# 반환 정보
# answer -> 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수

# [1] 생성한 정점의 번호인지 확인
# 나가는 edges가 2개 이상인데 들어오는 edges가 없음

# [2] 도넛 모양 그래프인지 확인
# v == e인 경우

# [3] 막대 모양 그래프인지 확인
# v = 1, e = 0인 핵이 존재

# [4] 8자 모양 그래프인지 확인
# 나가는 edges가 2개인 핵이 존재

# 초기 풀이 순서
# 1. vertex 중 edge가 2개 이상인 것들을 뽑음 (생성된 vertex이 될 수 있는 후보)
# 2. 후보 중 들어오는 edge가 없는 것을 생성된 vertex으로 판단 후 dict에서 제거
# 3. 나머지 후보들은 모두 8자 모양 그래프이고 dict에서 관련 vertex 모두 제거
# 4. edge가 없는 vertex는 막대 모양 그래프의 끝이므로 역산하면서 vertex 모두 제거
# 5. vertex와 edge의 수가 같으면 도넛 모양 그래프이므로 answer에 누적


# 수정한 풀이
# 1. vertex 중 들어오는 edge가 없고 나가는 edge만 있는 것을 생성된 vertex로 결정
# 2. 생성된 vertex를 제외하고 나가는 edge가 2개인 vertex는 8자 모양 그래프의 중심
# 3. 나가는 edge가 없는 vertex는 막대 모양 그래프의 끝
# 4. 생성된 vertex에서 나가는 edge에서 나머지 두 개를 빼면 도넛 모양 그래프의 수

def solution(edges):
    vertex_dict_i = dict()
    vertex_dict_o = dict()
    answer = [0 for _ in range(4)]
    # dictionary 초기화
    for i in range(len(edges)):
        if edges[i][0] not in vertex_dict_o:
            vertex_dict_o[edges[i][0]] = []
        if edges[i][1] not in vertex_dict_i:
            vertex_dict_i[edges[i][1]] = []
        vertex_dict_o[edges[i][0]].append(edges[i][1])
        vertex_dict_i[edges[i][1]].append(edges[i][0])
    
    o_keys = set(vertex_dict_o.keys())
    i_keys = set(vertex_dict_i.keys())

    for key in o_keys:
        # 생성된 vertex 찾기
        if len(vertex_dict_o[key]) >= 2 and key not in i_keys:
            answer[0] = key
        # 8자 모양 그래프의 중심 vertex 찾기
        elif len(vertex_dict_o[key]) >= 2:
            answer[3] += 1
    for key in i_keys:
        # 막대 모양 그래프의 머리 vertex 찾기
        if key not in o_keys:
            answer[2] += 1

    answer[1] = len(vertex_dict_o[answer[0]]) - answer[2] - answer[3]

    return answer


   