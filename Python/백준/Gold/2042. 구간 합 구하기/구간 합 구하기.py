import sys

input = sys.stdin.readline

# 선언부
def init(n_list: list[int]):
    global over_n
    n = len(n_list)
    while True:
        if n <= 2 ** over_n:
            break
        over_n += 1
    tree = [0 for _ in range(2 ** (over_n + 1))]

    for i in range(n):
        tree[2 ** over_n + i] = n_list[i]

    for i in range(2 ** over_n - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

    return tree

def update(before: int, after: int):
    new_before = 2 ** over_n + before - 1
    diff = after - segment_tree[new_before]
    while new_before != 0:
        segment_tree[new_before] += diff
        new_before //= 2

def question(start: int, end: int):
    new_start, new_end = 2 ** over_n + start - 1, 2 ** over_n + end - 1
    acc = 0
    while True:
        if new_start > new_end:
            break
        if new_start % 2 == 1:
            acc += segment_tree[new_start]
        if new_end % 2 == 0:
            acc += segment_tree[new_end]
        new_start, new_end = (new_start + 1) // 2, (new_end - 1) // 2
    return acc
        
# 구현부
N, M, K = map(int, input().split())
number_list, over_n = [], 0
for _ in range(N):
    number_list.append(int(input()))
segment_tree = init(number_list)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    elif a == 2:
        print(question(b, c))
