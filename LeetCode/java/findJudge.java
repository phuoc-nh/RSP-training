import java.util.ArrayList;
import java.util.List;

/**
 * findJudge
 */
public class findJudge {
    public static void main(String[] args) {
        int n = 2;
        int[][] trust = new int[][]{
            {1,2}
        };
        var a = findJudge(n, trust);
        System.out.println(a);
    }   

    static int findJudge(int n, int[][] trust) {
        List<Integer>[] adj = new ArrayList[n+1];

        for (int i = 0; i < n+1;i++) {
            adj[i] = new ArrayList<>();
        }

        for (var t: trust) {
            adj[t[0]].add(t[1]);
        }

        for (int i = 0; i < n+1;i++) {
            if (adj[i].isEmpty()) {
                var isJudge = true;
                for (int j = 1; j < n+1;j++) {
                    if (i == j) {
                        continue;
                    }
                    
                    if (!adj[j].contains(i)) {
                        isJudge = false;
                    }
                }

                return isJudge ? i : -1;
            }
        }

        return -1;
    }

}