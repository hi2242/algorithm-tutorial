# 문제 정보
# 불량 사용자 아이디 목록과 응모자 아이디 목록을 대조해서 제재 아이디 목록 산출
# 가능한 제재 아이디 목록의 경우의 수 세기

# 입력 정보
# user_id -> 이벤트 응모자 아이디 목록
# banned_id -> 불량 사용자 아이디 목록

# 반환 정보
# answer -> 당첨에서 제외되어야 할 제재 아이디 목록 경우의 수

import sys
from itertools import product

sys.setrecursionlimit(10**7)

def solution(user_id, banned_id):
    answer = set()
    possible_id = []
    for bid in banned_id:
        temp = []
        for uid in user_id:
            if compare(bid, uid):
                temp.append(uid)
        if len(temp) != 0:
            possible_id.append(temp)
    cartesian_list = product(*possible_id)
    for uid_list in cartesian_list:
        s_uid_list = set(uid_list)
        if len(s_uid_list) == len(possible_id):
            answer.add(frozenset(set(uid_list)))
    return len(answer)

def compare(a, b):
    la, lb = len(a), len(b)
    if la != lb:
        return False
    for i in range(la):
        if a[i] == "*":
            continue
        if a[i] != b[i]:
            return False
    return True
