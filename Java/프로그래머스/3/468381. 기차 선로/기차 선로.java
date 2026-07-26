import java.util.*;

class Solution {
    public static final int RAIL_TYPE_COUNT = 7;
    public static final int[] dr = {-1, 0, 1, 0};
    public static final int[] dc = {0, 1, 0, -1};
    
    public static int answer = 0;
    public static int n, m;

    // 바운더리 이내
    public static boolean isBoundaryIn(int r, int c) {
        return 0 < r && r <= n && 0 < c && c <= m;
    }

    // 선로의 next 방향 추출 함수 (연결 불가 시 -1 반환)
    public static int getNextDirection(int railType, int enterDirection) {
        int temp = -1;
        if (railType == 3 ||
            (railType == 1 && (enterDirection == 1 || enterDirection == 3)) ||
            (railType == 2 && (enterDirection == 0 || enterDirection == 2))) {
            temp = enterDirection;
        } else if (railType == 4) {
            if (enterDirection == 1) temp = 0;
            else if (enterDirection == 2) temp = 3;
        } else if (railType == 5) {
            if (enterDirection == 3) temp = 0;
            else if (enterDirection == 2) temp = 1;
        } else if (railType == 6) {
            if (enterDirection == 0) temp = 1;
            else if (enterDirection == 3) temp = 2;
        } else if (railType == 7) {
            if (enterDirection == 0) temp = 3;
            else if (enterDirection == 1) temp = 2;
        }
        return temp;
    }

    // 클리어 여부 및 모든 선로 순회 검증
    public static boolean isFinishValid(int r, int c, int[][] visited, int[][] visitCount) {
        // 목적지 도착 여부 확인
        if (r != n || c != m) return false;
        
        // 격자에 놓인 모든 선로를 지나갔는지 & 3번 선로를 두 번(십자) 지나갔는지 검증
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (visited[i][j] > 0) {
                    if (visited[i][j] == 3) {
                        if (visitCount[i][j] != 2) return false;
                    } else {
                        if (visitCount[i][j] != 1) return false;
                    }
                }
            }
        }
        return true;
    }

    // 백트래킹 로직 함수
    public static void backTracking(int r, int c, int railType, int enterDirection, int[][] grid, int[][] visited, int[][] visitCount) {
        // 복원을 위한 원본 상태 저장
        int originalValue = visited[r][c];
        visited[r][c] = railType;
        visitCount[r][c]++;

        int nd = getNextDirection(railType, enterDirection);

        // nd가 -1이 아니면 정상 진입(연결 가능)
        if (nd != -1) {
            // 목적지에 도달했을 때
            if (r == n && c == m) {
                if (isFinishValid(r, c, visited, visitCount)) {
                    answer++;
                }
            } else {
                int nr = r + dr[nd];
                int nc = c + dc[nd];

                // 바운더리 내부이고 장애물(-1)이 아닌 경우
                if (isBoundaryIn(nr, nc) && visited[nr][nc] != -1) {
                    if (visited[nr][nc] > 0) {
                        // 이미 놓인 선로가 3번(십자)이고 처음 방문한 경우 -> 교차 통과 허용
                        if (visited[nr][nc] == 3 && visitCount[nr][nc] == 1) {
                            backTracking(nr, nc, 3, nd, grid, visited, visitCount);
                        } 
                        // 맵에 원래 깔려있던 선로인데 아직 방문하지 않은 경우 -> 해당 선로 그대로 진행
                        else if (visitCount[nr][nc] == 0) {
                            backTracking(nr, nc, visited[nr][nc], nd, grid, visited, visitCount);
                        }
                    } 
                    else {
                        // 빈 칸(0)인 경우 -> 1~7번 선로 배치 시도
                        for (int nrt = 1; nrt <= RAIL_TYPE_COUNT; nrt++) {
                            backTracking(nr, nc, nrt, nd, grid, visited, visitCount);
                        }
                    }
                }
            }
        }

        // 백트래킹 복원
        visitCount[r][c]--;
        visited[r][c] = originalValue;
    }

    public int solution(int[][] grid) {
        n = grid.length;
        m = grid[0].length;
        answer = 0;
        
        int[][] visited = new int[n + 1][m + 1];
        int[][] visitCount = new int[n + 1][m + 1]; // 방문 횟수 및 모든 선로 순회 검증용
        
        for (int r = 1; r <= n; r++) {
            for (int c = 1; c <= m; c++) {
                visited[r][c] = grid[r - 1][c - 1];
            }
        }
        
        // (1,1)은 항상 1번 선로, 오른쪽(1) 방향으로 시작
        backTracking(1, 1, 1, 1, grid, visited, visitCount);

        return answer;
    }
}