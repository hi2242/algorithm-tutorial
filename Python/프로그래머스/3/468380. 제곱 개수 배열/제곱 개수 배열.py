# 문제 정보
# brr -> arr의 인덱스 순서대로 arr[i]를 배열 brr에 연속으로 arr[i]개씩 추가한다.
# arr: [2, 1, 5] -> brr: [2, 2, 1, 5, 5, 5, 5, 5]
# brr의 구간의 양 끝을 나타내는 l, r이 주어질 때 K와 C를 구한다.
# K = sum(brr[l - 1:r])
# C = (r - l + 1)인 brr의 부분 배열 합이 K인 부분 배열의 개수

# 입력 정보
# arr -> 1이상의 정수로 이루어진 길이가 N인 1차원 정수 배열
# l, r -> l번째 원소부터 r번째 원소까지의 합

# 반환 정보
# K -> brr의 l번째 원소부터 r번째 원소까지의 합
# C -> 길이가 (r - l + 1)인 brr의 부분 배열 중 합이 K인 부분 배열의 개수

def solution(arr, l, r):
    # K를 구하는 과정
    K = 0
    current_idx = 0
    
    for x in arr:
        block_start = current_idx
        block_end = current_idx + x - 1
        # 이번 블록에서는 어디가 overlap 되는지 정하는 로직
        # 목표 구간 [l-1, r-1]과 현재 블럭 구간의 겹치는 부분 계산
        overlap_start = max(block_start, l - 1)
        overlap_end = min(block_end, r - 1)
        
        # 겹치는 구간이 존재하면 그 길이만큼 값(x)을 곱해서 더함
        if overlap_start <= overlap_end:
            K += (overlap_end - overlap_start + 1) * x
            
        current_idx += x
        # 목표 구간을 넘어가면 조기 종료
        if current_idx >= r:
            break
    
    # C를 구하는 과정
    c_len = r - l + 1
    curr_sum = 0
    left_idx, left_cnt = 0, 0
    right_idx, right_cnt = 0, 0
    
    # 윈도우 크기(c_len)만큼만 배열에서 미리 뽑아 합계를 구함
    filled = 0
    while filled < c_len:
        add_cnt = min(arr[right_idx] - right_cnt, c_len - filled)
        curr_sum += add_cnt * arr[right_idx]
        right_cnt += add_cnt
        filled += add_cnt
        
        # 해당 블럭을 다 썼으면 다음 블럭으로 이동
        if right_cnt == arr[right_idx]:
            right_idx += 1
            right_cnt = 0
            
    # 첫 윈도우 합계가 K와 같다면 1에서 시작, 아니면 0
    C = 1 if curr_sum == K else 0
    
    while right_idx < len(arr):
        # 현재 블럭에서 더 갈 수 있는 남은 칸 수 (최소 점프 거리)
        left_remain = arr[left_idx] - left_cnt
        right_remain = arr[right_idx] - right_cnt
        
        distance = min(left_remain, right_remain)
        diff = arr[right_idx] - arr[left_idx]
        
        # 점프하는 과정에서 목표값 K를 만나는지 수학적 계산
        if diff == 0:
            if curr_sum == K:
                C += distance
        else:
            target_diff = K - curr_sum
            # K에 도달하기 위한 점프 횟수(steps)가 나누어 떨어지고,
            # 그 횟수가 이번에 점프하는 거리(distance) 안에 있는지 확인
            if target_diff % diff == 0:
                steps = target_diff // diff
                if 0 < steps <= distance: # 0보다 큰 이유는 출발점 중복 카운트 방지
                    C += 1
                    
        # 윈도우 상태 한 번에 점프
        curr_sum += diff * distance
        left_cnt += distance
        right_cnt += distance
        
        # 남은 칸 수를 다 소진한 쪽의 블럭 인덱스 넘기기
        if left_cnt == arr[left_idx]:
            left_idx += 1
            left_cnt = 0
        if right_cnt == arr[right_idx]:
            right_idx += 1
            right_cnt = 0
            
    return [K, C]