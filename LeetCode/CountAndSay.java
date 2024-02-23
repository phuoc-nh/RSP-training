package LeetCode;

public class CountAndSay {
    public static void main(String[] args) {
        solution(4);
    }

    static String solution(int n) {
        var res = new String[n+1];
        for (int i =0; i < n+1; i++) {
            res[i] = "";
        }
        res[1] = "1";

        for (int i = 2; i<n+1;i++) {
            int j = 1;
            int count = 1;
            String cur = res[i-1];
            while (j < cur.length()) {
                if (cur.charAt(j-1) == cur.charAt(j)) {
                    count++;
                } else {
//                   count + number
                    res[i] += (String.valueOf(count) + cur.charAt(j-1));
                    count = 1;
                }
                j++;
            }
//            System.out.println("cur " + cur);
//            System.out.println("j "  + j);
//            System.out.println("???/ " + String.valueOf(count) + cur.charAt(j-1));

            res[i] += (String.valueOf(count) + cur.charAt(j-1));

//            System.out.println(">>>> =================== " + res[i]);
        }

//        System.out.println(res[n]);
        return res[n];
    }
}
