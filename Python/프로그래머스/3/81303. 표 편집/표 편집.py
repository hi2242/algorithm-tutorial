# 문제 정보
# 명령어 기반으로 표의 행을 선택/삭제/복구
# 파란색으로 칠해진 칸은 현재 선택된 행을 의미
# 한 번에 한 행만 선택 가능 + 표의 범위 (0행 ~ 마지막 행)을 벗어날 수 없음
# 명령어
    # "U X" -> 현재 선택된 행에서 X칸 위의 행 선택
    # "D X" -> 현재 선택된 행에서 X칸 아래의 행 선택
    # "C" -> 현재 선택된 행 삭제 + 바로 아래 행 선택 (만약 마지막 행이면 바로 윗 행 선택)
    # "Z" -> 가장 최근에 삭제된 행 복구 (현재 선택된 행은 바뀌지 않음)

# 입력 정보
# n -> 행의 개수
# k -> 처음 선택된 행의 위치
# cmd -> 수행한 명령어 문자열 배열

# 반환 정보
# answer -> 표의 수행 전후를 비교하여 삭제되지 않은 행은 O, 삭제된 행은 X로 표시한 문자열

from collections import deque

def solution(n, k, cmd):
    answer = []
    excel = {i: [i - 1, i + 1] for i in range(n)}
    excel[0][0], excel[n - 1][1] = None, None
    curr_pos = k
    remove_dq = deque()
    
    def move_cell(direction, diff):
        nonlocal curr_pos
        for i in range(diff):
            curr_pos = excel[curr_pos][0] if direction == "U" else excel[curr_pos][1]
    
    def remove_cell():
        nonlocal n, curr_pos, excel, remove_dq
        remove_dq.appendleft((curr_pos, excel[curr_pos]))
        prev_pos, next_pos = excel[curr_pos]
        temp = excel[curr_pos][0] if excel[curr_pos][1] is None else excel[curr_pos][1]
        if prev_pos is not None:
            excel[prev_pos][1] = next_pos
        if next_pos is not None:
            excel[next_pos][0] = prev_pos
        del excel[curr_pos]
            
        curr_pos = temp
    
    def revert_cell():
        nonlocal excel, remove_dq, curr_pos
        pos, value = remove_dq.popleft()
        prev_pos, next_pos = value
        if prev_pos is not None:
            excel[prev_pos][1] = pos
        if next_pos is not None:
            excel[next_pos][0] = pos
        excel[pos] = value
    
    for c in cmd:
        if c[0] == "U" or c[0] == "D":
            t, v = c.split()
            move_cell(t, int(v))
        elif c[0] == "C":
            remove_cell()
        elif c[0] == "Z":
            revert_cell()
    
    def compare():
        nonlocal excel, answer
        for i in range(n):
            if excel.get(i) is not None:
                answer.append("O")
            else:
                answer.append("X")
                
    compare()
    return "".join(answer)