import java.util.*;

public class FindCheapestPrice {
    public static void main(String[] args) {
        var n = 5;
        var flight = new int[][] {
                {1,2,10},
                {2,0,7},
                {1,3,8},
                {4,0,10},
                {3,4,2},
                {4,2,10},
                {0,3,3},
                {3,1,6},
                {2,4,5},
        };
        var src = 0;
        var dst = 4;
        var k = 1;
        System.out.println(">>>>>>> " + findCheapestPrice(n, flight, src, dst, k));
    }

    static int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        var dist = new int[n];
        ArrayList<int[]>[] adj = new ArrayList[n];

        for (int i =0; i < n; i++) {
            dist[i] = Integer.MAX_VALUE;
            adj[i] = new ArrayList();
        }

        for (var flight: flights) {
            int u = flight[0], v = flight[1], cost = flight[2];
            var temp = new int[] {
                    v,
                    cost
            };
            adj[u].add(temp);
        }

        Queue<int[]> queue = new LinkedList<>(); // add remove peek
        dist[src] = 0;

        queue.add(new int[] {src, 0});
        queue.isEmpty();
        int stops = 0;
        int res = Integer.MAX_VALUE;
        while (!queue.isEmpty()) {
            var size = queue.size();
            while (size != 0) {
                int[] top = queue.remove();
                var u = top[0];
                var uDist = top[1];

                for (var nei: adj[u]) {
                    var v = nei[0];
                    var vDist = nei[1];

                    if (uDist + vDist <= dist[v]) {
                        if (stops <= k) {

                            res = Math.min(res, uDist + vDist);
                        }
                        dist[v] = uDist + vDist;
                        queue.add(new int[] {v, dist[v]});
                    }
                }

                size--;
            }
            stops++;
        }
        for (var d: dist) {
            System.out.println("Ddd " + d);
        }

        return res != Integer.MAX_VALUE ? res : -1;
    }
}
