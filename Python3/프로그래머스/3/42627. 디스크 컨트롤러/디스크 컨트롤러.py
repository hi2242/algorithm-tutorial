# 기본 정보
# 하드디스크 -> 한 번에 하나의 작업 수행
# 우선순위 디스크 컨트롤러 동작
    # 1. 대기 큐: 작업 요청이 들어오면 작업의 번호, 작업의 요청 시각, 작업의 소요 시간을 저장 (처음엔 비어 있음)
    # 2. 하드디스크가 작업을 하지 않고 대기 큐가 비어 있지 않다면 대기 큐에서 가장 우선순위가 높은 작업을 꺼냄 (1등(작업의 소요시간이 짧은 것) -> 2등(작업의 요청 시각이 빠른 것) -> 3등(작업의 번호가 작은 것))
    # 3. 작업을 시작하면 작업이 끝날 때까지 그 작업만 수행
    # 4. 작업을 마치는 시점과 다른 작업 요청이 들어오는 시점이 겹치면 대기 큐에서 저장 후 꺼내기 순서로 진행, 작업을 마치는 시점에 다른 작업이 들어오지 않으면 대기 큐에서 꺼내서 진행 (이 동기적 순서에 소요 시간은 필요 없음)

# 입력 정보
# jobs -> [[요청 시각, 소요 시간], [1, 9], [3, 5]]

import heapq

curr_t = 0

# pq가 비었을 때 curr_t을 다음 요청 시각까지 갱신하면서 업데이트를 강제로 시켜주는 함수
# 작업이 끝나고 다음 작업까지의 시간이 비었을 때 발생하는 예외 처리
def empty_hq_hard_push(k, n, sorted_jobs, hq):
    global curr_t
    work_num, request_time, need_time = sorted_jobs[k]
    if curr_t < request_time:
        curr_t = request_time
    return update_queue(k, n, sorted_jobs, hq)
    
def update_queue(k, n, sorted_jobs, hq):
    t = k
    # 이전에 마지막으로 pq에 저장했던 위치에서 반복문 시작
    for i in range(k, n):
        # 현재 시각보다 이전에 요청된 jobs를 모두 pq에 추가
        work_num, request_time, need_time = sorted_jobs[i]
        if request_time > curr_t:
            return t
        heapq.heappush(hq, (need_time, request_time, work_num))
        t += 1
    return t
    
def solution(jobs):
    global curr_t
    answer = 0
    sorted_jobs = []
    hq = []
    n = len(jobs)
    for i in range(n):
        request_time, need_time = jobs[i]
        sorted_jobs.append([i, request_time, need_time])
        
    sorted_jobs.sort(key = lambda x: (x[1], x[2]))
    return_time_acc = 0
    k = empty_hq_hard_push(0, n, sorted_jobs, hq)
    while True:
        if k == n and not hq:
            break
        if hq:
            need_time, request_time, work_num = heapq.heappop(hq)
            curr_t += need_time
            return_time_acc += curr_t - request_time
            k = update_queue(k, n, sorted_jobs, hq)
        else:
            k = empty_hq_hard_push(k, n, sorted_jobs, hq)
    # 최종 리스트의 평균 시간 계산 후 반환
    answer = return_time_acc // n
    return answer