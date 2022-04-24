package programmers;

import java.util.Arrays;

public class 입국심사 {

    public long solution(int n, int[] times) {
        long min = 0L;
        long max = (1000000000L * ((n / times.length) + 1));
        long cur = (min + max) / 2;
        while (min != max) {
            long number = 0;
            for (int time : times) {
                number += (cur / time);
            }
            if (number >= n) {
                max = cur;
            } else {
                min = cur+1;
            }
            cur = (min + max) / 2;
        }
        return cur;
    }
}
