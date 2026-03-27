import sys

input = sys.stdin.readline

# 선언부
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.left = left
        self.right = right
        self.value = value
        
def minification():
    temp = sorted(list(set(a)))
    rank_to_val = {}
    val_to_rank = {}
    for i in range(len(temp)):
        rank_to_val[i + 1] = temp[i]
        val_to_rank[temp[i]] = i + 1
    result = [0] + [val_to_rank[i] for i in a]
    return result, rank_to_val

    
def init(each, start, end):
    if start == end:
        if start == each:
            return Node(value=1)
        else:
            return Node(value=0)
    mid = (start + end) // 2
    left = init(each, start, mid)
    right = init(each, mid + 1, end)
    return Node(left, right, left.value + right.value)

def update(prev_node, each, start, end):
    if start == end == each:
        return Node(value=prev_node.value + 1)
    mid = (start + end) // 2
    if start <= each <= mid:
        left = update(prev_node.left, each, start, mid)
        right = prev_node.right
    elif mid + 1 <= each <= end:
        left = prev_node.left
        right = update(prev_node.right, each, mid + 1, end)
    return Node(left, right, left.value + right.value)

def query(max_node, min_node, start, end, k):
    if start == end:
        return start
    mid = (start + end) // 2
    left_count = max_node.left.value - min_node.left.value
    if k <= left_count:
        result = query(max_node.left, min_node.left, start, mid, k)
    else:
        result = query(max_node.right, min_node.right, mid + 1, end, k - left_count)
    return result
        
def Q(i, j, k):
    idx = query(root_list[j], root_list[i - 1], 1, max_rank, k)
    print(rank_to_val[idx])
    
# 구현부
n, m = map(int, input().split())
a = list(map(int, input().split()))
new_a, rank_to_val = minification()

max_rank = len(rank_to_val)
root_list = [init(0, 1, max_rank)]
for i in range(1, n + 1):
    root_list.append(update(root_list[-1], new_a[i], 1, max_rank))

for _ in range(m):
    i, j, k = map(int, input().split())
    Q(i, j, k)