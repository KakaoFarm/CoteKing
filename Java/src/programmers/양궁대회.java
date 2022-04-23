package programmers;

public class 양궁대회 {

    static int maxScore = -1;
    static int[] maxArrows;
    static Target[] targets = new Target[10];

    public int[] solution(int n, int[] info) {
        int apeachScore = 0;
        for (int i=0; i<10; i++) {
            if (info[i] > 0) {
                apeachScore += (10 - i);
            }
            int cost = info[i] + 1;
            int score = cost > 1 ? (10 - i) * 2 : 10 - i;
            targets[i] = new Target(cost, score);
        }
        calculate(0, n, 0, new int[]{0,0,0,0,0,0,0,0,0,0,0});
        if (maxScore <= apeachScore) {
            return new int[]{-1};
        }
        return maxArrows;
    }

    class Target {
        int cost;
        int score;

        public Target(int cost, int score) {
            this.cost = cost;
            this.score = score;
        }
    }

    private void calculate(int cur, int n, int score, int[] arrows) {
        if (cur == 10) {
            if (score >= maxScore) {
                int[] newArrows = arrows.clone();
                newArrows[10] = n;
                if (score > maxScore || curIsBetter(maxArrows, newArrows)) {
                    maxScore = score;
                    maxArrows = newArrows;
                }
            }
        } else {
            if (n >= targets[cur].cost) {
                int[] newArrows = arrows.clone();
                newArrows[cur] = targets[cur].cost;
                calculate(cur + 1, n - targets[cur].cost, score + targets[cur].score, newArrows);
            }
            calculate(cur + 1, n, score, arrows);
        }
    }

    private boolean curIsBetter(int[] old, int[] cur) {
        for (int i=10; i>=0; i--) {
            if (old[i] > cur[i]) {
                return false;
            } else if (old[i] < cur[i]) {
                return true;
            }
        }
        return false;
    }
}
