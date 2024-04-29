import java.util.Stack;

public class canva2 {
	public static void main(String[] args) {
		System.out.println(getFinalString("AWAWSSG"));
		System.out.println(getFinalString("AWS"));
		System.out.println(getFinalString("AAWSWS"));
	}

	// remove AWS in string
	static String getFinalString(String s) {
		char[] arr = s.toCharArray();
		Stack<Character> stack = new Stack<>();
		for (char c : arr) {
			if (stack.isEmpty()) {
				stack.push(c);
			} else {
				if (stack.size() >= 2 && stack.get(stack.size() - 1) == 'W' && stack.get(stack.size() - 2) == 'A' && c == 'S') {
					stack.pop();
					stack.pop();
				} else {
					stack.push(c);
				}
			}
		}

		String res = "";
		if (stack.isEmpty()) {
			return "-1";
		}

		for (char c : stack) {
			res += c;
		}

		return res.toString();
	}
}
