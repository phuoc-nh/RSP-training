import java.util.HashMap;
import java.util.Map;

public class MaxFrequencyElements {
    public static void main(String[] args) {
        int[] nums = {
            1,2,2,3,1,4
        };
        Map<Integer, Integer> counter = new HashMap<>();
        for (int n: nums) {
            if (!counter.containsKey(n)) {
                counter.put(n,0);
            }
            counter.put(n, counter.get(n) + 1);
        }
        int maxCount = Integer.MIN_VALUE;
        for (var n: counter.values()) {
            maxCount = Math.max(n, maxCount);
        }
        int res = 0;
        for (var n: counter.values()) {
            if (n == maxCount) {
                res += n;
            }
        }
        System.out.println(res);

        System.out.println(counter);
    }
}
