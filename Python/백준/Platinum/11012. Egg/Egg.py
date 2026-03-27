import sys
from bisect import bisect_right

input = sys.stdin.readline

# 선언부
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.left = left
        self.right = right
        self.value = value

def init(x: int, start: int, end: int):
    if start == end:
        if start == x:
            return Node(value=1)
        else:
            return Node(value=0)

    mid = (start + end) // 2
    left = init(x=x, start=start, end=mid)
    right = init(x=x, start=mid + 1, end=end)
    return Node(left=left, right=right, value=left.value + right.value)

def update(prev_node: Node, x: int, start: int, end: int):
    if start == end == x:
        return Node(value=prev_node.value + 1)
    mid = (start + end) // 2
    if start <= x <= mid:
        left = update(prev_node= prev_node.left, x=x, start=start, end=mid)
        right = prev_node.right
    elif mid + 1 <= x <= end:
        left = prev_node.left
        right = update(prev_node= prev_node.right, x=x, start=mid + 1, end=end)
    return Node(left=left, right=right, value=left.value + right.value)

def query(node:Node, start: int, end: int, left: int, right: int):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return node.value
    mid = (start + end) // 2
    return query(node.left, start, mid, left, right) + query(node.right, mid + 1, end, left, right)
    
# 구현부
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    result = 0
    root_list = []
    version_list = []
    p_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        p_list.append((x, y))
    p_list.sort(key=lambda x: x[1])
    x_max, y_max = -1, -1
    for p in p_list:
        x_max = max(x_max, p[0])
        y_max = max(y_max, p[1])
    root_list.append(init(-1, 0, x_max))
    version_list.append(0)
    y_max = max(y_max, len(p_list))
    for px, py in p_list:
        if version_list[-1] == py:
            root_list[-1] = update(root_list[-1], px, 0, x_max)
        else:
            root_list.append(update(root_list[-1], px, 0, x_max))
            version_list.append(py)
        
    for _ in range(m):
        l, r, b, t = map(int, input().split())
        temp_t, temp_b = bisect_right(version_list, t) - 1, bisect_right(version_list, b - 1) - 1   
        result += (query(root_list[temp_t], 0, x_max, l, r) - query(root_list[temp_b], 0, x_max, l, r))
    print(result)
        