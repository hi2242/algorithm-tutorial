import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 선언부
def init(n_list: list[int]):
    global k
    n = len(n_list)
    while True:
        if n <= 2 ** k:
            break
        k += 1
    tree = [0 for _ in range(2 ** (k + 1))]
    for i in range(n):
        tree[2 ** k + i] = i + 1

    for i in range(2 ** k - 1, 0, -1):
        if temp[tree[i * 2]] <= temp[tree[i * 2 + 1]]:
            tree[i] = tree[i * 2]
        else:
            tree[i] = tree[i * 2 + 1]
    return tree


def question(start: int, end: int):
    t_start, t_end = 2 ** k + start - 1, 2 ** k + end - 1
    minimum = 0
    while True:
        if t_start > t_end:
            break
        if t_start % 2 == 1 and temp[segment_tree[minimum]] >= temp[segment_tree[t_start]]:
            minimum = t_start
        if t_end % 2 == 0 and temp[segment_tree[minimum]] >= temp[segment_tree[t_end]]:
            minimum = t_end
        t_start, t_end = (t_start + 1) // 2, (t_end - 1) // 2
    return segment_tree[minimum]


def solve(start: int, end: int):
    if start < 1 or start > len(temp) - 1 or end < 1 or end > len(temp) - 1:
        return 0
    if start >= end:
        return temp[start]
    min_idx = question(start, end)
    return max(solve(start, min_idx - 1), temp[min_idx] * (end - start + 1), solve(min_idx + 1, end))


# 구현부
while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break
    number_list = []
    for i in range(1, len(line)):
        number_list.append(line[i])
    temp = [int(1e9)]
    for n in number_list:
        temp.append(n)
    k = 0
    segment_tree = init(number_list)
    print(solve(1, len(number_list)))
