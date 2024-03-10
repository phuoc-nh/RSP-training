import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class Intersection {
    public static void main(String[] args) {


    }

    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> s = new HashSet<>();
        for (var n: nums1) {
            s.add(n);
        }

        HashSet<Integer> res = new HashSet<>();

        for (var n: nums2) {
            if (s.contains(n)) {
                res.add(n);
            }
        }

        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}
