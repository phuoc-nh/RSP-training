import java.sql.Array;
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
//		char[][] sudoku = new char[][]{
//				{'5','3','.','.','7','.','.','.','.'}
//				,{'6','.','.','1','9','5','.','.','.'}
//				,{'.','9','8','.','.','.','.','6','.'}
//				,{'8','.','.','.','6','.','.','.','3'}
//				,{'4','.','.','8','.','3','.','.','1'}
//				,{'7','.','.','.','2','.','.','.','6'}
//				,{'.','6','.','.','.','.','2','8','.'}
//				,{'.','.','.','4','1','9','.','.','5'}
//				,{'.','.','.','.','8','.','.','7','9'}
//		};
//		var res = isValidSudoku(sudoku);
//		System.out.println(">>> res " + res);

//		int[] nums = new int[] {0,3,7,2,5,8,4,6,0,1};
//
//		longestConsecutive(nums);

//		int[] nums = new int[] {
//				-1, 0
//		};
//		int target= -1;
//		var res = twoSum2(nums, target);

//		int[] nums = new int[] {
////				-1,0,1,2,-1,-4
////				1,-1,-1,0,
////				0,0,0
////				0,1,1
//				-2,0,0,2,2
//		};
////[1,-1,-1,0]
//		var res = threeSum(nums);
//
//		System.out.println("> res " + res);


//		int[] nums = new int[] {
//				-2,-1,-1,1,1,  2,2,0,4,5
//		};
//		var left = Arrays.copyOfRange(nums, 0, nums.length / 2);
//		var right = Arrays.copyOfRange(nums, nums.length / 2, nums.length);
//
//		System.out.println(Arrays.toString(left));
//		System.out.println(Arrays.toString(right));

//		var res = sortArray(nums);
//		System.out.println(">> res"  + Arrays.toString(res));

//		int target = 0;
//		var res = fourSum(nums, target);
//		System.out.println(">> res " + res);


//		mergeSort(nums);


//		int[] nums1 = new int[] {
//				0
//		};
//		int[] nums2 = new int[] {
//			1
//		};
//		int m = 0;
//		int n = 1;
//
//		merge(nums1, m, nums2, n);

//		String hayStack = "leetcode";
//		String needle = "leeto";
//
//		var res = strStr(hayStack, needle);
//
//		System.out.println(">>> " + res);


//		int[] nums = new int[] {
//				0,0,1,1,1,1,2,3,3
//		};
//
//		var r = removeDuplicates2(nums);
		int num = 1994;
		var res = intToRoman(num);
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

	static public int longestConsecutive(int[] nums) {
		Set<Integer> set = new HashSet<>();

		for (int n: nums) {
			set.add(n);
		}

		int res = 0;

		for (int s: set) {
			if (!set.contains(s-1)) {
				int temp = s;
				int tres = 0;
				while (set.contains(temp)) {
					tres++;
					temp++;
				}

				res = Math.max(res, tres);
			}
		}

		System.out.println(">?>" + res);

		return res;
	}

	static public int[] twoSum2(int[] numbers, int target) {
		int l = 0;
		int r = numbers.length - 1;

		while (l < r) {
			if (numbers[l] + numbers[r] == target) {
				return new int[] {l+1, r+1};
			} else if (numbers[l] + numbers[r] > target) {
				r--;
			} else {
				l++;
			}
		}

		return new int[]{};
	}

	static public List<List<Integer>> threeSum(int[] nums) {
		Arrays.sort(nums);
		int len = nums.length;
		List<List<Integer>> res = new ArrayList<>();
		System.out.println(">>>" + Arrays.toString(nums));

		for (int i = 0; i < len; i++) {
			int l = i+1;
			int r = len - 1;

			if (i > 0 && nums[i] == nums[i-1]) {
				continue;
			}

			while (l < r) {
				if (nums[i] + nums[l] + nums[r] == 0) {
					var t = Arrays.asList(nums[i], nums[l], nums[r]);
					res.add(t);
					l++;
					r--;

					while (nums[l] == nums[l-1]) {
						l++;
					}
					while ( nums[r] == nums[r+1]) {
						r--;
					}


				} else if (nums[i] + nums[l] + nums[r] > 0) {
					r--;
				} else {
					l++;
				}
			}
		}

		return res;

	}

	static public int threeSumClosest(int[] nums, int target) {

		Arrays.sort(nums);

		var outerDiff = Integer.MAX_VALUE;
		var resSum = 0;

		for (int i = 0; i < nums.length; i++) {

			if (i > 0 && nums[i] == nums[i-1]) {
				continue;
			}

			var l = i+1;
			var r = nums.length - 1;

			while (l < r) {
				var sum = nums[i] + nums[l] + nums[r];
				var diff = Math.abs(sum - target);
				if (diff < outerDiff) {
					outerDiff = diff;
					resSum = sum;
				}

				if (sum > target) {
					r--;
				} else if (sum < target) {
					l--;
				} else {
					return 0;
				}
			}
		}


		return resSum;

	}

	static public List<List<Integer>> fourSum(int[] nums, int target) {
		List<List<Integer>> res = new ArrayList<>();
		Arrays.sort(nums);
		System.out.println(">>>" + Arrays.toString(nums));

		for (int i = 0; i < nums.length; i++) {
			if (i > 1 && nums[i] == nums[i-1]) {
				continue;
			}
			for (int j = i+1; j < nums.length; j++) {

				if (j > i+1 && nums[j] == nums[j-1]) {
					continue;
				}

				var l = j + 1;
				var r = nums.length - 1;

				while (l < r) {
					if (nums[i] + nums[j] + nums[l] + nums[r] == target) {
						var t = Arrays.asList(nums[i] , nums[j] , nums[l] , nums[r]);
						res.add(t);
						r--;
						l++;

						while (r > 0 && nums[r] == nums[r+1]) {
							r--;
						}
						while (l < nums.length && nums[l] == nums[l-1]) {
							l++;
						}
					} else if (nums[i] + nums[j] + nums[l] + nums[r] > target) {
						r--;
					} else {
						l++;
					}


				}
			}
		}

		return  res;
	}

	static public int[] sortArray(int[] nums) {

		return mergeSort(nums, 0, nums.length - 1);
	}

	static public int[] mergeSort(int[] arr, int l, int r) {
		if (l == r) {
			return arr;
		}

		var mid = (l + r) / 2;

		mergeSort(arr, l, mid);
		mergeSort(arr, mid+1, r);

		merge(arr, l, mid, r);

		return arr;
	};

	static public void merge(int[] arr, int l, int m, int r) {
		var left = Arrays.copyOfRange(arr, l, m+1);
		var right = Arrays.copyOfRange(arr, m+1, r+1);

		var j = 0;
		var k = 0;
		var i = l;

		while (j < left.length && k < right.length) {
			if (left[j] <= right[k]) {
				arr[i] = left[j];
				j++;
			} else {
				arr[i] = right[k];
				k++;
			}
			i++;
		}

		while (j < left.length) {
			arr[i] = left[j];
			j++;
			i++;
		}

		while (k < right.length) {
			arr[i] = right[k];
			k++;
			i++;
		}
//		if (a == n)
	}

	static public void merge(int[] nums1, int m, int[] nums2, int n) {
		int cur = m + n - 1;
		int p1 = m - 1;
		int p2 = n - 1;
		while (cur >= 0) {
			if (p1 < 0) {
				nums1[cur] = nums2[p2];
				p2--;
				cur--;
				continue;
			}

			if (p2 < 0) {
				nums1[cur] = nums1[p1];
				p1--;
				cur--;
				continue;
			}

			if (nums1[p1] >= nums2[p2]) {
				nums1[cur] = nums1[p1];
				p1--;
			} else {
				nums1[cur] = nums2[p2];
				p2--;
			}

			cur--;
		}

//		System.out.println(">> " + Arrays.toString(nums1));
	}

	static public int strStr(String haystack, String needle) {
		var lenHay = haystack.length();
		var lenNeedle = needle.length();

		var diff = lenHay - lenNeedle;

		if (diff < 0) return  -1;

		for (int i = 0; i < diff + 1; i++ ) {
			var p1 = i;
			var p2 = 0;

			while (p1 < lenHay && p2 < lenNeedle && haystack.charAt(p1) == needle.charAt(p2)) {
				p1++;
				p2++;
			}

			if (p2 == lenNeedle) return  i;
		}

		return -1;
	}

	static public int removeDuplicates(int[] nums) {
		var count = 1;

		for (int i = 1; i < nums.length; i++) {
			if (nums[i] == nums[i-1]) {
				continue;
			} else {
				nums[count] = nums[i];
				count++;
			}
		}

//		System.out.println(Arrays.toString(nums));
//		System.out.println(count);
		return count;
	}

	static public int removeDuplicates2(int[] nums) {
		var count = 1;
		var p = 1;
		for (int i = 1; i < nums.length; i++) {
			if (nums[i] == nums[i-1]) {
				count++;
				if (count <= 2) {
					nums[p] = nums[i];
					p++;
				}
			} else {
				count = 1;
				nums[p] = nums[i];
				p++;
			}

		}
//		System.out.println(count);
//		System.out.println(count);
//		System.out.printf("p >> " + p);
//		System.out.printf("p nums  " + Arrays.toString(nums));
		return p;
	}

	static public String intToRoman(int num) {
		List<String> roman = Arrays.asList(
				"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV","I"
		);
		List<Integer> romanInt = Arrays.asList(
				1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4,1
		);

		List<Map<String, Integer>> map = new ArrayList<>();

//		map.put()
		StringBuilder res = new StringBuilder();

		while (num != 0) {
			for (int i = 0; i < romanInt.toArray().length; i++) {
				var intPart = num / romanInt.get(i);
				if (intPart > 0) {
//					var temp = roman.get(i).repeat(intPart);
					res.append(roman.get(i).repeat(intPart));
					num = num - intPart * romanInt.get(i);

				}
			}
		}

		System.out.println(res.toString());

		return  res.toString();

	}

}