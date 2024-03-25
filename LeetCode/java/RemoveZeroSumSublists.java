import java.util.Stack;

public class RemoveZeroSumSublists {
    public static void main(String[] args) {
        var input = new int[]{
                1,2,3,0,-3,-2
        };

        removeZeroSumSublists(input);
    }

    static public int[] removeZeroSumSublists(int[] s) {
        Stack<Integer> stack = new Stack<>();

        for (var n: s) {
            if (stack.isEmpty()) {
                stack.add(n);
                continue;
            }

            var temp = n;
            Stack<Integer> mStack = new Stack<>();
            while (!stack.isEmpty() && temp * stack.peek() < 0) {
                var top = stack.pop();
                temp += top;
                mStack.add(top);
            }

            if (temp != 0) {
                while (!mStack.isEmpty()) {
                    stack.add(mStack.pop());
                }
                stack.add(n);
            }
        }
        int[] res = {};
        System.out.println(stack);
        return res;
    }
}
