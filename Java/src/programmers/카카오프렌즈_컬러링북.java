package programmers;

import java.util.LinkedList;
import java.util.Queue;

public class 카카오프렌즈_컬러링북 {

    int[][] picture;
    boolean[][] visited;
    final int[] dx = new int[]{-1, 1, 0, 0};
    final int[] dy = new int[]{0, 0, -1, 1};
    int n;
    int m;

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        this.picture = picture;
        visited = new boolean[m][n];
        this.n = n;
        this.m = m;

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                int cnt = bfs(i, j);
                if (cnt > 0) {
                    numberOfArea += 1;
                    if (cnt > maxSizeOfOneArea) {
                        maxSizeOfOneArea = cnt;
                    }
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    public int bfs(int x, int y) {
        int color = picture[x][y];
        if (color == 0) {
            return 0;
        }
        if (visited[x][y]) {
            return 0;
        }
        Queue<Pos> queue = new LinkedList<>();
        queue.offer(new Pos(x, y));
        visited[x][y] = true;
        int cnt = 0;
        while (!queue.isEmpty()) {
            Pos cur = queue.poll();
            cnt += 1;
            for (int i=0; i<4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (0 <= nx && nx < m && 0 <= ny && ny < n && picture[nx][ny] == color && !visited[nx][ny]) {
                    Pos next = new Pos(nx, ny);
                    queue.offer(next);
                    visited[next.x][next.y] = true;
                }
            }
        }
        return cnt;
    }

    static class Pos {
        int x;
        int y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
