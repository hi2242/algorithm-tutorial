# 문제 정보
# 테이블의 퍼즐 조각을 게임 보드의 빈 공간에 올리기
# 1x1 칸으로 이루어진 정사각 격자 게임 보드 및 테이블
# 빈칸 채우기 규칙
    # 조각은 한 번에 하나씩 채워 넣기
    # 조각 회전 가능
    # 조각 뒤집기 불가능
    # 게임 보드에 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안됨
# 규칙에 맞게 최대한 게임 보드에 퍼즐을 넣기

# 입력 정보
# game_board -> 현재 게임 보드의 상태
# table -> 테이블 위에 놓인 퍼즐 조각의 상태

# 반환 정보
# answer -> 퍼즐을 통해 채울 수 있는 최대 칸 수

# 풀이 순서
# 1. table의 퍼즐 타입 정의 후 배열(puzzles)에 저장
# 2. game_board의 빈 칸을 돌려가면서 puzzles에 있는지 확인

import sys
sys.setrecursionlimit(10**6)

def get_blocks(board, target):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    blocks = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def dfs(r, c, block):
        visited[r][c] = True
        block.append((r, c))
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and board[nr][nc] == target:
                    dfs(nr, nc, block)

    for i in range(n):
        for j in range(n):
            if board[i][j] == target and not visited[i][j]:
                block = []
                dfs(i, j, block)
                blocks.append(block)
    
    return blocks

def normalize(block):
    min_r = min(x[0] for x in block)
    min_c = min(x[1] for x in block)
    return sorted([(r - min_r, c - min_c) for r, c in block])

def rotate(block):
    rotated = [(c, -r) for r, c in block]
    return normalize(rotated)

def solution(game_board, table):
    empty_spaces = [normalize(b) for b in get_blocks(game_board, 0)]
    puzzles = [normalize(b) for b in get_blocks(table, 1)]
    
    answer = 0
    used = [False] * len(puzzles)
    
    for space in empty_spaces:
        for i, puzzle in enumerate(puzzles):
            if used[i]: 
                continue
            
            if len(space) != len(puzzle): 
                continue
                
            matched = False
            rotated_puzzle = puzzle
            
            for _ in range(4):
                if space == rotated_puzzle:
                    used[i] = True
                    answer += len(puzzle)
                    matched = True
                    break
                rotated_puzzle = rotate(rotated_puzzle)
                
            if matched:
                break
                
    return answer