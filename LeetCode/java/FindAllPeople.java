package LeetCode;

import java.util.*;

public class FindAllPeople {
    public static void main(String[] args) {
        int n = 5;
        int[][] meetings = {
                {3,4,2},
                {1,2,1},
                {2,3,1},
        };
        int firstPerson = 1;

        System.out.println(findAllPeople(n, meetings, firstPerson));

    }
    public static List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {

        Map <Integer, Map<Integer, List<Integer>>> timeToAdjMap = new HashMap<>();
        for (var m: meetings)  {
            var src = m[0];
            var dst = m[1];
            var time = m[2];

            if (!timeToAdjMap.containsKey(time)) {
                Map<Integer, List<Integer>> innerMap = new HashMap<>();
                timeToAdjMap.put(time, innerMap);
            }

            var innerMap = timeToAdjMap.get(time);
            innerMap.computeIfAbsent(src, value -> new ArrayList<>()).add(dst);
            innerMap.computeIfAbsent(dst, value -> new ArrayList<>()).add(src);

        }

        Set<Integer> res = new HashSet<>();
        res.add(0);
        res.add(firstPerson);
        var sortKeys = new ArrayList();
        sortKeys.addAll(sortKeys);
        Arrays.sort(sortKeys.toArray());


        Set<Integer> testSet = new HashSet<>();
        testSet.add(4);
        testSet.add(1);
        testSet.add(3);
        testSet.add(6);

        var test = new ArrayList();
        test.addAll(testSet);
        Arrays.sort(test.toArray());
        System.out.println("test " + test);


        for (var time: sortKeys) {
            Set<Integer> visited = new HashSet<>();
            Queue<Integer> q = new LinkedList();
            for (var s: timeToAdjMap.get(time).keySet()) {
                if (res.contains(s)) {
                    q.offer(s);
//                    dfs(s, timeToAdjMap.get(time), visited, res);
                    var adj = timeToAdjMap.get(time);
                    while (!q.isEmpty()) {
                        var top = q.poll();
                        for (var v: adj.get(top)) {
                            if (!visited.contains(v)) {
                                visited.add(v);
                                res.add(v);
                            }
                        }
                    }
                }
            }
        }

        List<Integer> returnV = new ArrayList<>();
        returnV.addAll(res);
        return returnV;
    }

    public static void dfs(int s, Map<Integer, List<Integer>> adj, Set<Integer> visited, Set<Integer> res) {
        if (visited.contains(s)) {
            return;
        }
        visited.add(s);
        res.add(s);

        for (var v: adj.get(s)) {
            dfs(v, adj, visited, res);
        }
    }
}
