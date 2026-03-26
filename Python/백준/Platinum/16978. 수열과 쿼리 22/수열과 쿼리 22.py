import sys

input = sys.stdin.readline

# 선언부
class Node:
    def __init__(self, left = None, right = None, value = 0):
        self.left = left
        self.right = right
        self.value = value
        
def init(start: int, end: int):
    if start == end:
        if start > N:
            temp = 0
        else:
            temp = A[start]
        return Node(value = temp)
    mid = (start + end) // 2
    left = init(start, mid)
    right = init(mid + 1, end)
    return Node(left, right, left.value + right.value)

def update(prev_node: Node, index: int, value: int, start: int, end: int):
    if start == end:
        return Node(value = value)
    mid = (start + end) // 2
    if index <= mid:
        left = update(prev_node.left, index, value, start, mid)
        right = prev_node.right
    else:
        left = prev_node.left
        right = update(prev_node.right, index, value, mid + 1, end)
    return Node(left, right, left.value + right.value)
        
def query(node: Node, start: int, end: int, left: int, right: int):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return node.value
    mid = (start + end) // 2
    return query(node.left, start, mid, left, right) + query(node.right, mid + 1, end, left, right)
    
# 구현부
N = int(input())
A = [0] + list(map(int, input().split()))
exp_n = 0
while True:
    if N <= 2 ** exp_n:
        break
    exp_n += 1
root_list = []
root_list.append(init(1, 2 ** exp_n))
M = int(input())
for _ in range(M):
    line = list(map(int, input().split()))
    if line[0] == 1:
        root_list.append(update(root_list[-1], line[1], line[2], 1, 2 ** exp_n))
    elif line[0] == 2:
        print(query(root_list[line[1]], 1, 2 ** exp_n, line[2], line[3]))
        