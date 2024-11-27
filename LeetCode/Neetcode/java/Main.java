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

//		int[] nums = {1,2,2,3,3,3};
//		int k = 2;
//
//		var res = topKFrequent(nums, k);

//		var strs = Arrays.asList("we","say",":","yes","!@#$%^&*()");
//		var code = encode(strs);
//
//		var dec = decode(code);

//		var nums = new int[] {-1,0,1,2,3};
//		var res = productExceptSelf(nums);


		char[][] sudoku = new char[][]{
				{'5','3','.','.','7','.','.','.','.'}
				,{'6','.','.','1','9','5','.','.','.'}
				,{'.','9','8','.','.','.','.','6','.'}
				,{'8','.','.','.','6','.','.','.','3'}
				,{'4','.','.','8','.','3','.','.','1'}
				,{'7','.','.','.','2','.','.','.','6'}
				,{'.','6','.','.','.','.','2','8','.'}
				,{'.','.','.','4','1','9','.','.','5'}
				,{'.','.','.','.','8','.','.','7','9'}
		};

		var res = isValidSudoku(sudoku);
		System.out.println(">>> res " + res);


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

	static public String encode(List<String> strs) {
		StringBuilder res = new StringBuilder();
		for (String s: strs) {
			res.append(s.length());
			res.append("#");
			res.append(s);
		}


		return res.toString();
	}

	static  List<String> decode(String str) {
		List<String> res = new ArrayList<>();
		var i = 0;
		while (i < str.length()) {
			var j = i;
			while (str.charAt(j) != '#') {
				j++;
			}
			var range = str.substring(i, j);
			var nextStop = j+1 + Integer.parseInt(range);
			StringBuilder piece = new StringBuilder();
			i = j + 1;
			for (int k = j+1; k < nextStop; k++) {
				piece.append(str.charAt(k));
				i++;
			}

			res.add(piece.toString());
		}

		System.out.println(res);
		return  res;
	}

	static public int[] productExceptSelf(int[] nums) {


		var len = nums.length;

		if (len == 1) {
			return nums;
		}

		var prefix = new int[len];
		var suffix = new int[len];

		prefix[0] = nums[0];
		suffix[len-1] = nums[len-1];

//		System.out.println(Arrays.toString(nums));

		for (int i = 1; i < len; i++) {
			prefix[i] = nums[i] * prefix[i-1];
		}

		for (int i = len-2; i > -1; i--) {
			suffix[i] = nums[i] * suffix[i+1];
		}

//		System.out.println(">>>" + Arrays.toString(prefix));
//		System.out.println(">>>" + Arrays.toString(suffix));

		var res = new int[len];

		res[0] = suffix[1];
		res[len-1] = prefix[len-2];

		for (int i = 1; i < len -1; i++) {
			res[i] = prefix[i-1] * suffix[i+1];
		}

//		System.out.printf("res" + Arrays.toString(res));


		return res;

	}

	static public boolean isValidSudoku(char[][] board) {
//		check row
		for (int i = 0; i < 9; i++) {
			HashSet set = new HashSet();
			for (int j = 0; j < 9; j++) {
				System.out.println(">> row " + board[i][j]);
				if (board[i][j] == '.') {
					continue;
				}
				if (set.contains(board[i][j])) {
					return false;
				}
				set.add(board[i][j]);
			}
		}

		for (int i = 0; i < 9; i++) {
			HashSet set = new HashSet();
			for (int j = 0; j < 9; j++) {
				System.out.println("col " + board[j][i]);
				if (board[j][i] == '.') {
					continue;
				}
				if (set.contains(board[j][i])) {
					return false;
				}
				set.add(board[j][i]);
			}
		}

		for (int i = 0; i < 9; i = i + 3) {
			for (int j = 0; j < 9; j = j + 3) {
				HashSet set = new HashSet();
				for (int k = i; k < i + 3; k++) {
					for (int l = j; l < j + 3; l++) {
						if (board[k][l] == '.') {
							continue;
						}
						if (set.contains(board[k][l])) {
							return false;
						}
						set.add(board[k][l]);
					}
				}
			}
		}

		return true;
	}

}