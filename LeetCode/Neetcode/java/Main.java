import java.util.*;

public class Main {
	public static void main(String[] args) {
//		int[] nums = {3, 4, 5, 6};
//		var target = 7;
//
//		twoSum(nums , target);

// 		Primitive types boolean, byte, char, short, int, long, float, double
//		String[] strs = {"act","pots","tops","cat","stop","hat"};
//
//		var res = optimalGroupAnagrams(strs);
//
//		System.out.println(res);

		int[] nums = {1,2,2,3,3,3};
		int k = 2;

		var res = topKFrequent(nums, k);
	}

	static public boolean isAnagram(String s, String t) {
		HashMap<Character, Integer> countS = new HashMap<>();
		HashMap<Character, Integer> countT = new HashMap<>();

		for (int i = 0; i < s.length(); i++) {
			countS.put(s.charAt(i), countS.getOrDefault(s.charAt(i), 0) + 1);
		}

		for (int i = 0; i < t.length(); i++) {
			countT.put(t.charAt((i)), countT.getOrDefault(t.charAt(i), 0) + 1);
		}
		return countS.equals(countT);

	}

	static public int[] twoSum(int[] nums, int target) {
		HashMap<Integer, Integer> m = new HashMap<>();

		for (int i = 0; i < nums.length; i++) {
			m.put(nums[i], i);
		}

		for (int i = 0; i < nums.length; i++) {
			var diff = target - nums[i];

			if (m.containsKey(diff) && m.get(diff) != i) {
				return new int[]{i, m.get(diff)};
			}

		}

		return new int[0];
	}

	public static String sortString(String str) {
		var chars = str.toCharArray();
		Arrays.sort(chars);

		return new String(chars);
	}
//  nlognm
	static public List<List<String>> groupAnagrams(String[] strs) {
		HashMap<String, List<String>> dup = new HashMap<>();

		for (String s: strs) {
			var sortedS = sortString(s);

			if (dup.containsKey(sortedS)) {
				dup.get(sortedS).add(s);
			} else {
				dup.put(sortedS, new ArrayList<>());

				dup.get(sortedS).add(s);
			}
		}

		return new ArrayList<>(dup.values());

	}

	static public List<List<String>> optimalGroupAnagrams(String[] strs) {
		HashMap<String, List<String>> dup = new HashMap<>();

		for (String s: strs) {
			int[] hash = new int[26];
			for (char c: s.toCharArray()) {
				hash[c - 'a'] += 1;
			}

//			String stringHash = hash.toString();
			String stringHash = Arrays.toString(hash);
			System.out.println("stringHash" + stringHash);

			if (dup.containsKey(stringHash)) {
				dup.get(stringHash).add(s);
			} else {
				dup.put(stringHash, new ArrayList<>());
				dup.get(stringHash).add(s);
			}
		}

		return new ArrayList<>(dup.values());

	}


	static public int[] topKFrequent(int[] nums, int k) {
		HashMap<Integer, Integer> counter = new HashMap<>();

		for (var n: nums) {
			if (!counter.containsKey(n)) {
				counter.put(n, 0);
			}

			counter.put(n, counter.get(n) + 1);
		}

		System.out.println(counter);

		PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]); // count, value

		for (var key: counter.keySet()) {
			pq.offer(new int[]{counter.get(key), key});

			if (pq.size() > k) {
				pq.poll();
			}
		}

		int[] res = new int[k];

		for (int i = 0; i < k; i ++) {
			res[i] = pq.poll()[1];
		}

//		System.out.printf(Arrays.toString((res)));

		return res;
 	}
}