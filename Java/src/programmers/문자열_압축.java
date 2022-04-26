package programmers;

public class 문자열_압축 {

    public int solution(String s) {

        int n = s.length();
        int answer = n;
        for (int k=1; k<=(n/2); k++) {
            String temp = "";
            int i = 0;
            int result = n;
            int cnt = 0;
            while (i+k <= n) {
                String cur = s.substring(i, i + k);
                if (cur.equals(temp)) {
                    if (cnt == 1 || cnt == 9 || cnt == 99 || cnt == 999) {
                        result -= (k-1);
                    } else {
                        result -= k;
                    }
                    cnt += 1;
                } else {
                    temp = cur;
                    cnt = 1;
                }
                i += k;
            }
            if (result < answer) {
                answer = result;
            }
        }
        return answer;
    }
}
