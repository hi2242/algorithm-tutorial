import sys

input = sys.stdin.readline

# 선언부
def init(n: int, n_list: list[int]):
    global exp_n
    while True:
        if n <= 2 ** exp_n:
            break
        exp_n += 1
    tree = [0 for _ in range(2 ** (exp_n + 1))]
    for i in range(n):
        tree[2 ** exp_n + i] = n_list[i]
    for i in range(2 ** exp_n - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]
    return tree

def push_down(node: int, start: int, end: int):
    if lazy[node] != 0:
        segment_tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0
    
def question(node: int, start: int, end: int, left: int, right: int):
    push_down(node, start, end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return segment_tree[node]
    mid = (start + end) // 2
    return question(node * 2, start, mid, left, right) + question(node * 2 + 1, mid + 1, end, left, right)
    
def update(node: int, start: int, end: int, left: int, right: int, diff: int):
    push_down(node, start, end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        lazy[node] += diff
        push_down(node, start, end)
        return
    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, diff)
    update(node * 2 + 1, mid + 1, end, left, right, diff)
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]
    
# 구현부
N, M, K = map(int, input().split())
number_list = []
for _ in range(N):
    number_list.append(int(input()))
exp_n = 0
segment_tree = init(N, number_list)
lazy = [0 for _ in range(len(segment_tree))]
for _ in range(M + K):
    line = list(map(int, input().split()))
    if line[0] == 1:
        update(1, 1, 2 ** exp_n, line[1], line[2], line[3])
    elif line[0] == 2:
        print(question(1, 1, 2 ** exp_n, line[1], line[2]))
        