import sys

input = sys.stdin.readline

# 선언부
def init(n: int, n_list: list[int]):
    global k
    while True:
        if n <= 2 ** k:
            break
        k += 1
        
    min_tree = [int(1e9) for _ in range(2 ** (k + 1))]
    max_tree = [0 for _ in range(2 ** (k + 1))]
    
    for i in range(n):
        min_tree[2 ** k + i] = n_list[i]
        max_tree[2 ** k + i] = n_list[i]
    for i in range(2 ** k - 1, 0, -1):
        min_tree[i] = min(min_tree[2 * i], min_tree[2 * i + 1])
        max_tree[i] = max(max_tree[2 * i], max_tree[2 * i + 1])
    return (min_tree, max_tree)

def question(a: int, b: int):
    start, end = 2 ** k + a - 1, 2 ** k + b - 1
    minimum, maximum = int(1e9), 0
    while True:
        if start > end:
            break
        if start % 2 == 1:
            minimum = min(minimum, min_tree[start])
            maximum = max(maximum, max_tree[start])
        if end % 2 == 0:
            minimum = min(minimum, min_tree[end])
            maximum = max(maximum, max_tree[end])
        start, end = (start + 1) // 2, (end - 1) // 2
    print(minimum, maximum)
        
# 구현부
N, M = map(int, input().split())
number_list = []
k = 0
for _ in range(N):
    number_list.append(int(input()))
min_tree, max_tree = init(N, number_list)
for _ in range(M):
    a, b = map(int, input().split())
    question(a, b)