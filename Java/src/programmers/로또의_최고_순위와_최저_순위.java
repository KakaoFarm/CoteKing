package programmers;

import java.util.Arrays;

public class 로또의_최고_순위와_최저_순위 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{44, 1, 0, 0, 31, 25}, new int[]{31, 10, 45, 1, 6, 19})));
    }

    public static int[] solution(int[] lottos, int[] win_nums) {
        int count = 0;
        int zero = 0;
        for (int num : lottos) {
            if (contains(win_nums, num)) {
                count++;
            }
            if (num == 0) {
                zero++;
            }
        }
        int lowRank = Math.min(6, 7 - count);
        int highRank = Math.min(6, 7 - count - zero);
        return new int[]{highRank, lowRank};
    }

    public static boolean contains(int[] arr, int target) {
        for (int num : arr) {
            if (num == target) {
                return true;
            }
        }
        return false;
    }
}
