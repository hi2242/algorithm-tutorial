import sys

input = sys.stdin.readline

# 선언부
MAX_NODES = 100000 * 40
L = [0] * MAX_NODES
R = [0] * MAX_NODES
V = [0] * MAX_NODES
node_idx = 0

class Node:
    def __init__(self, left=None, right=None, value=0):
        self.left = left
        self.right = right
        self.value = value

def get_new_node():
    global node_idx
    node_idx += 1
    return node_idx
    
def minification():
    temp = sorted(list(set(a)))
    rank_to_val = {}
    val_to_rank = {}
    for i in range(len(temp)):
        rank_to_val[i + 1] = temp[i]
        val_to_rank[temp[i]] = i + 1
    result = [0] + [val_to_rank[i] for i in a]
    return result, rank_to_val

def update(prev_node, each, start, end):
    curr_node = get_new_node()
    V[curr_node] = V[prev_node] + 1
    if start == end:
        return curr_node
    mid = (start + end) // 2

    if start <= each <= mid:
        L[curr_node] = update(L[prev_node], each, start, mid)
        R[curr_node] = R[prev_node]
    elif mid + 1 <= each <= end:
        L[curr_node] = L[prev_node]
        R[curr_node] = update(R[prev_node], each, mid + 1, end)
    return curr_node

def query(max_node, min_node, start, end, k):
    if start == end:
        return start
    mid = (start + end) // 2
    left_count = V[L[max_node]] - V[L[min_node]]
    if k <= left_count:
        result = query(L[max_node], L[min_node], start, mid, k)
    else:
        result = query(R[max_node], R[min_node], mid + 1, end, k - left_count)
    return result
        
def Q(i, j, k):
    idx = query(root_list[j], root_list[i - 1], 1, max_rank, k)
    print(rank_to_val[idx])
    
# 구현부
n, m = map(int, input().split())
a = list(map(int, input().split()))
new_a, rank_to_val = minification()

max_rank = len(rank_to_val)
root_list = [0]
for i in range(1, n + 1):
    root_list.append(update(root_list[-1], new_a[i], 1, max_rank))

for _ in range(m):
    i, j, k = map(int, input().split())
    Q(i, j, k)