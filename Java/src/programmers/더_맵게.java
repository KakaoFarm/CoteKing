package programmers;

import java.util.PriorityQueue;

public class 더_맵게 {

    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int value : scoville) {
            heap.offer(value);
        }

        int answer = 0;
        while (!heap.isEmpty()) {
            int low1 = heap.poll();
            if (low1 >= K) {
                return answer;
            }
            if (heap.isEmpty()) {
                break;
            }
            int low2 = heap.poll();
            int newOne = low1 + (low2 * 2);
            answer++;
            heap.offer(newOne);
        }
        return -1;
    }
}
