package programmers;

import java.util.LinkedList;
import java.util.Queue;

public class 거리두기_확인하기 {

    private final int[] dx = {-1, 1, 0, 0};
    private final int[] dy = {0, 0, -1, 1};

    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        for (int i=0; i<5; i++) {
            Case aCase = new Case(places[i]);
            if (aCase.isOk()) {
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }
        return answer;
    }

    class Case {
        private final String[][] board = new String[5][];

        public Case(String[] s) {
            for (int i=0; i<5; i++) {
                board[i] = s[i].split("");
            }
        }

        public boolean isOk() {
            for (int i=0; i<5; i++) {
                for (int j=0; j<5; j++) {
                    if (board[i][j].equals("P") && !check(i, j)) {
                        return false;
                    }
                }
            }
            return true;
        }

        public boolean check(int x, int y) {
            boolean[][] visited = new boolean[5][5];
            Queue<Element> queue = new LinkedList<>();
            queue.add(new Element(x, y, 0));
            while (!queue.isEmpty()) {
                Element now = queue.poll();
                visited[now.x][now.y] = true;
                for (int i=0; i<4; i++) {
                    int nx = now.x + dx[i];
                    int ny = now.y + dy[i];
                    if (now.cnt <= 1 && 0 <= nx && nx < 5 && 0 <= ny && ny < 5 && !board[nx][ny].equals("X") && !visited[nx][ny]) {
                        if (board[nx][ny].equals("P")) {
                            return false;
                        }
                        queue.add(new Element(nx, ny, now.cnt+1));
                    }
                }
            }
            return true;
        }
    }

    class Element {
        int x;
        int y;
        int cnt;

        public Element(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
}
