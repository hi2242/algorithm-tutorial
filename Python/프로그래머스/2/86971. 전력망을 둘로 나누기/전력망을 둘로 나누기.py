# 문제 정보
# n개의 송전탑이 하나의 트리로 연결
# 선 중 하나를 끊어 2개로 분할
# 두 전력망의 송전탑 개수를 비슷하게 맞춤

# 입력 정보
# n -> 송전탑 개수
# wires -> 전선 정보

# 반환 정보
# answer -> 두 전력망의 송전탑 개수 차이

# 풀이 순서
# 1. Union-Find를 통해 전력망 연결
# 2. 완전탐색으로 선을 하나씩 누락시키기
# 3. 루프를 다 돌면 나뉜 전력망이 몇개인지 세기
# 4. 두 전력망의 송전탑 개수 차이 계산
import sys

sys.setrecursionlimit(100000)

INF = float('inf')

def solution(n, wires):
    answer = INF
    parents = [i for i in range(n + 1)]
    wires_n = len(wires)
    for i in range(wires_n):
        parents = [i for i in range(n + 1)]
        for j in range(wires_n):
            if i == j:
                continue
            union(wires[j][0], wires[j][1], parents)
        answer = min(sort_parents(parents, n), answer)
    return answer

def union(a, b, parents):
    root_a = find(a, parents)
    root_b = find(b, parents)
    
    if root_a == root_b:
        return
    parents[root_a] = root_b

def find(x, parents):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x], parents)
    return parents[x]

def sort_parents(parents, n):
    a, b = find(1, parents), 0
    a_c, b_c = 1, 0
    for i in range(2, n + 1):
        temp = find(i, parents)
        if b == 0 and a != temp:
            b = temp
        if a == temp:
            a_c += 1
        else:
            b_c += 1

    return abs(a_c - b_c)