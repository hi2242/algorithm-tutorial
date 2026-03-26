import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)

def each_init(n: int, n_list: list[int]):
    tree = [0 for _ in range(2 ** (exp_n + 1))]
    for i in range(n):
        tree[2 ** exp_n + i] = n_list[i]
    for i in range(2 ** exp_n - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]
    return tree
    
def init(n: int, grid: list[list[int]]):
    global exp_n
    while True:
        if n <= 2 ** exp_n:
            break
        exp_n += 1
    tree = [[0 for _ in range(2 ** (exp_n + 1))] for _ in range(2 ** (exp_n + 1))]
    for i in range(n):
        tree[2 ** exp_n + i] = each_init(n, grid[i])

    for i in range(2 ** exp_n - 1, 0, -1):
        for j in range(1, 2 ** (exp_n + 1)):
            tree[i][j] = tree[2 * i][j] + tree[2 * i + 1][j]
    return tree

def each_question(r: int, start: int, end: int):
    acc = 0
    while True:
        if start > end:
            break
        if start % 2 == 1:
            acc += segment_tree[r][start]
        if end % 2 == 0:
            acc += segment_tree[r][end]
        start, end = (start + 1) // 2, (end - 1) // 2
    return acc
        
def question(r_start: int, c_start: int, r_end: int, c_end: int):
    nr_start, nr_end = 2 ** exp_n + r_start - 1, 2 ** exp_n + r_end - 1
    nc_start, nc_end = 2 ** exp_n + c_start - 1, 2 ** exp_n + c_end - 1
    acc = 0
    while True:
        if nr_start > nr_end:
            break
        if nr_start % 2 == 1:
            acc += each_question(nr_start, nc_start, nc_end)
        if nr_end % 2 == 0:
            acc += each_question(nr_end, nc_start, nc_end)
        nr_start, nr_end = (nr_start + 1) // 2, (nr_end - 1) // 2
    return acc

def each_update(r: int, c: int, diff: int):
    temp = c
    while True:
        if temp < 1:
            break
        segment_tree[r][temp] += diff
        temp //= 2
        
def update(r: int, c: int, value: int):
    nr, nc = 2 ** exp_n + r - 1, 2 ** exp_n + c - 1
    diff = value - segment_tree[nr][nc]
    while True:
        if nr < 1:
            break
        each_update(nr, nc, diff)
        nr //= 2
        
# 구현부
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
exp_n = 0
segment_tree = init(N, grid)
for _ in range(M):
    line = list(map(int, input().split()))
    if line[0] == 0:
        update(line[1], line[2], line[3])
    elif line[0] == 1:
        print(question(line[1], line[2], line[3], line[4]))
        