//package LeetCode;
//
//import java.lang.reflect.Array;
//import java.util.ArrayList;
//import java.util.Arrays;
//import java.util.Collections;
//import java.util.HashMap;
//import java.util.HashSet;
//import java.util.LinkedList;
//import java.util.List;
//import java.util.Map;
//import java.util.PriorityQueue;
//import java.util.Set;
//import java.util.Stack;
//
//class HelloWorld {
//    public static void main(String[] args) {
//        System.out.println("Hello, World!");
//        for (int i = 0; i < args.length; i++) {
//
//        }
//        int k = Integer.MIN_VALUE;
//        int km = Integer.MAX_VALUE;
//        List<Integer> list = new ArrayList<>();
//        list.addAll(Arrays.asList(1, 2, 3));
//
//        Collections.min(list);
//        // Init array with all Zero
//        var dp = new int[3];
//        String word1 = "acb";
//        for (char c : word1.toCharArray()) { // Use toCharArray for string to be iterable
//            System.out.println(c); // Print a, c, b
//        }
//        // Stack
//        Stack<Character> st = new Stack<>();
//        st.push('x');
//        Character ab = st.pop();
//        st.peek(); // See the top value of Stack
//
//        // init PriorityQueue with int value
//        var pqInt = new PriorityQueue<Integer>();
//        pqInt.offer(1); // Insert into pq
//        pqInt.isEmpty(); // check empty pq
//        pqInt.poll(); // Pop pq
//        pqInt.peek(); // See the top value of pq
//        // Init PriorityQueue with list value
//        var pqList = new PriorityQueue<long[]>((a, b) -> a[0] != b[0] ? Long.compare(a[0], b[0]): Long.compare(a[1], b[1]));
//        // pqList.peek()[1];
//        pqList.offer(new long[]{1,2});
//        var room = pqList.peek()[1];
//        // Cast type
//        int x = (int) pqList.poll()[1];
//        // init variable
//        int res = 0;
//
//        int[][] meetings = {{1,2}, {3,4}};
//        Arrays.sort(meetings, (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
//
//        // ======================= HASH map ===============================
//        Map<Character, Integer> wordMap = new HashMap<>();
//        wordMap.put('c', wordMap.getOrDefault('c', 0) + 1);
//        // infer integer from 'a' -> 'a' - 'a' = 0 NO DOUBLE QUOTE, SINGLE QUOTE ONLY
//        // Check if hash map contains value x
//        boolean hashX = wordMap.containsValue('x');
//
//
//
//        Set<Integer> onlyInNums1 = new HashSet<> ();
//        onlyInNums1.add(1);
//        // Convert hash set to list
//        new ArrayList<>(onlyInNums1);
//        onlyInNums1.contains(1);
//
//
//        // Queue which is call LinkedList in Java
//        var slideWindow = new LinkedList<Integer>();
//        slideWindow.addLast(1);
//        slideWindow.removeFirst();
//        slideWindow.size();
//
//
//        // 2D array
//        int [][] d = new int[2][3];
//        for (int[] arr: d) {
//            Arrays.fill(arr, 1);
//        }
//
//        // Convert int list to string list
//        var intList = new int[]{1, 2};
//
//        List<String> stringList = intList.
//
//
//
//    }
//
//    public String largestNumber(int[] nums) {
//        List<String> stringList = new ArrayList<>(); // List dynamic size, usually hold Object like String, Integer .... Slow acc
//        String[] s = new String[]{}; // Fixed size, hold primitive and Object, Direct faster access
//
//        for (int i = 0; i < nums.length;i++) {
//            s[i] = String.valueOf((nums[i]));
//        }
//
//        Arrays.sort(s, (a, b) -> (b+a).compareTo(a+b));
//        return String.join("", s);
//    }
//}