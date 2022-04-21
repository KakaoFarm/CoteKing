package programmers;

public class 카펫 {

    public int[] solution(int brown, int yellow) {
        int sum = (brown / 2) + 2;
        int size = brown + yellow;
        for (int width=1; width<sum; width++) {
            if (width * (sum - width) == size) {
                return new int[]{Math.max(width, sum - width), Math.min(width, sum - width)};
            }
        }
        return new int[]{0, 0};
    }
}
