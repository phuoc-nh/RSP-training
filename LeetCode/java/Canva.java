import java.util.Stack;

public class Canva {

	public static void main(String[] args) {
		System.out.println(getMaxDeletions("ULUDUULLUD"));
	}
	// U Up
	// D Down
	// R Right
	// L Left
	static int getMaxDeletions(String s) {
		Stack<Character> stack = new Stack<>();
		char[] arr = s.toCharArray();
		int res = 0;
		for (char c : arr) {
			if (stack.isEmpty()) {
				stack.push(c);
			} else {
				// loop back to the previous element
				int curSize = stack.size();
				System.out.println(stack);
				System.out.println(c);
				boolean found = false;
				for (int i = curSize - 1; i >= 0; i--) {
					if (c == 'U' && stack.get(i) == 'D') {
						stack.remove(i);
						res += 2;
						found = true;
						break;
					} else if (c == 'D' && stack.get(i) == 'U') {
						stack.remove(i);
						res += 2;
						found = true;
						break;
					} else if (c == 'R' && stack.get(i) == 'L') {
						stack.remove(i);
						res += 2;
						found = true;
						break;
					} else if (c == 'L' && stack.get(i) == 'R') {
						stack.remove(i);
						res += 2;
						found = true;
						break;
					}
				}
				if (!found) {
					stack.push(c);
				}
			}
		}

		return res;
	}
}